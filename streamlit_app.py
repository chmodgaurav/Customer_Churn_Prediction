import streamlit as st
import pandas as pd
import joblib
import os

MODEL_PATH = os.path.join('models', 'churn_model.pkl')
FEATURES_PATH = os.path.join('models', 'feature_names.pkl')

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURES_PATH)
    return model, feature_names

model, feature_names = load_model()

st.set_page_config(
    page_title='Customer Churn Predictor',
    page_icon='📉',
    layout='wide',
)

st.title('📉 Customer Churn Prediction')
st.markdown(
    'Enter customer details and predict churn probability using the trained model.'
)

with st.form('prediction_form'):
    col1, col2 = st.columns(2)

    with col1:
        tenure = st.slider('Tenure (months)', 0, 72, 12)
        monthly_charges = st.number_input('Monthly Charges ($)', min_value=0.0, value=70.0, step=1.0)
        total_charges = st.number_input('Total Charges ($)', min_value=0.0, value=700.0, step=1.0)
        senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
        internet_service = st.selectbox('Internet Service', ['No', 'DSL', 'Fiber optic'])
        contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])

    with col2:
        online_security = st.checkbox('Online Security')
        online_backup = st.checkbox('Online Backup')
        device_protection = st.checkbox('Device Protection')
        tech_support = st.checkbox('Tech Support')
        streaming_tv = st.checkbox('Streaming TV')
        streaming_movies = st.checkbox('Streaming Movies')
        paperless_billing = st.selectbox('Paperless Billing', ['No', 'Yes'])
        payment_method = st.selectbox(
            'Payment Method',
            ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check']
        )

    submitted = st.form_submit_button('Predict Churn')

if submitted:
    input_data = {
        'tenure': tenure,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges,
        'senior_citizen': 1 if senior_citizen == 'Yes' else 0,
        'internet_service_dsl': 1 if internet_service == 'DSL' else 0,
        'internet_service_fiber_optic': 1 if internet_service == 'Fiber optic' else 0,
        'contract_month_to_month': 1 if contract == 'Month-to-month' else 0,
        'contract_one_year': 1 if contract == 'One year' else 0,
        'contract_two_year': 1 if contract == 'Two year' else 0,
        'online_security_yes': 1 if online_security else 0,
        'online_backup_yes': 1 if online_backup else 0,
        'device_protection_yes': 1 if device_protection else 0,
        'tech_support_yes': 1 if tech_support else 0,
        'streaming_tv_yes': 1 if streaming_tv else 0,
        'streaming_movies_yes': 1 if streaming_movies else 0,
        'paperless_billing_yes': 1 if paperless_billing == 'Yes' else 0,
        'payment_method_credit_card': 1 if payment_method == 'Credit card (automatic)' else 0,
        'payment_method_electronic_check': 1 if payment_method == 'Electronic check' else 0,
        'payment_method_mailed_check': 1 if payment_method == 'Mailed check' else 0,
        'tenure_group_0_1_year': 1 if tenure <= 12 else 0,
        'tenure_group_1_2_years': 1 if 12 < tenure <= 24 else 0,
        'tenure_group_2_4_years': 1 if 24 < tenure <= 48 else 0,
        'tenure_group_4_6_years': 1 if tenure > 48 else 0,
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    prediction_proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    risk_level = 'High' if prediction_proba > 0.7 else 'Medium' if prediction_proba > 0.4 else 'Low'

    col1, col2 = st.columns([3, 2])
    with col1:
        st.metric('Churn Prediction', 'Yes' if prediction == 1 else 'No')
        st.metric('Risk Level', risk_level)
    with col2:
        st.progress(int(prediction_proba * 100))
        st.write(f'**Probability:** {prediction_proba:.2%}')

    if prediction == 1:
        st.warning('This customer is likely to churn. Consider retention strategies.')
    else:
        st.success('This customer is likely to stay.')

    st.markdown('---')
    st.write('### Input features used for prediction')
    st.json(input_data)

st.sidebar.header('About')
st.sidebar.write(
    'This Streamlit app uses the trained churn model saved in `models/churn_model.pkl` to predict customer churn probability.'
)
st.sidebar.write('Run with: `streamlit run streamlit_app.py`')
