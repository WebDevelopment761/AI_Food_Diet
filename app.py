import streamlit as st
import pandas as pd

# १. पेज कॉन्फिगरेशन आणि डिझाईन
st.set_page_config(page_title="AI Diet & Nutrition Planner", page_icon="🥗", layout="centered")

st.title("🥗 AI Diet & Nutrition Planner")
st.write("तुमची माहिती भरा आणि तुमचा वैयक्तिक डाएट प्लॅन मिळवा!")

# २. युझरकडून इनपुट घेणे (User Input)
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("वय (Age)", min_value=10, max_value=100, value=25)
    gender = st.selectbox("लिंग (Gender)", ["पुरुष (Male)", "महिला (Female)"])
    height = st.number_input("उंची (Height in cm)", min_value=100, max_value=250, value=170)

with col2:
    weight = st.number_input("वजन (Weight in kg)", min_value=30, max_value=200, value=65)
    activity = st.selectbox("शारीरिक हालचाल (Activity Level)", [
        "कमी (Sedentary - No Exercise)",
        "मध्यम (Moderate - 3-5 days/week)",
        "जास्त (Active - Daily Exercise)"
    ])
    goal = st.selectbox("तुमचे ध्येय (Your Goal)", ["वजन कमी करणे (Weight Loss)", "वजन वाढवणे (Weight Gain)", "फिट राहणे (Maintain Weight)"])

# ३. डाएट रिकमेंडेशन लॉजिक (Rule-Based ML Engine)
if st.button("डाएट प्लॅन तयार करा 🚀"):
    
    # BMR (Basal Metabolic Rate) कॅल्क्युलेशन (Harris-Benedict Equation)
    if gender == "पुरुष (Male)":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
    # Activity Multiplier
    if "कमी" in activity:
        tdee = bmr * 1.2
    elif "मध्यम" in activity:
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.75
        
    # Goal नुसार कॅलरीज ठरवणे
    if goal == "वजन कमी करणे (Weight Loss)":
        target_calories = tdee - 500
        protein = weight * 1.5
        carbs = (target_calories * 0.4) / 4
        fats = (target_calories * 0.25) / 9
    elif goal == "वजन वाढवणे (Weight Gain)":
        target_calories = tdee + 500
        protein = weight * 2.0
        carbs = (target_calories * 0.5) / 4
        fats = (target_calories * 0.25) / 9
    else:
        target_calories = tdee
        protein = weight * 1.2
        carbs = (target_calories * 0.45) / 4
        fats = (target_calories * 0.25) / 9

    # ४. रिझल्ट स्क्रीनवर दाखवणे
    st.success("🎯 तुमचा डेली न्यूट्रिशन रिपोर्ट तयार आहे!")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    metrics_col1.metric("कॅलरीज (Calories)", f"{int(target_calories)} kcal")
    metrics_col2.metric("प्रोटीन (Protein)", f"{int(protein)} g")
    metrics_col3.metric("कार्ब्स (Carbs)", f"{int(carbs)} g")
    metrics_col4.metric("फॅट्स (Fats)", f"{int(fats)} g")
    
    # ५. डाएट प्लॅन सजेशन (Sample Diet Recommendation Dataset)
    st.subheader("🍽️ सुचवलेला आहार (Suggested Diet Plan)")
    
    if goal == "वजन कमी करणे (Weight Loss)":
        st.info("**सकाळचा नाश्ता:** ओट्स, सुका मेवा आणि ग्रीन टी.\n\n"
                "**दुपारचे जेवण:** २ चपात्या, १ वाटी वरण, पालेभाजी आणि सॅलड.\n\n"
                "**संध्याकाळचा नाश्ता:** भाजलेले हरभरे किंवा मखाना.\n\n"
                "**रात्रीचे जेवण:** उकडलेले मूग/चिकन सॅलड किंवा सूप आणि १ चपाती.")
    elif goal == "वजन वाढवणे (Weight Gain)":
        st.info("**सकाळचा नाश्ता:** बनाना शेक, पीनट बटर टोस्ट आणि उकडलेली अंडी/पनीर.\n\n"
                "**दुपारचे जेवण:** ३ चपात्या, जास्त भात, वरण, पनीर/चिकन आणि दही.\n\n"
                "**संध्याकाळचा नाश्ता:** मूठभर बदाम, अक्रोड आणि १ ग्लास दूध.\n\n"
                "**रात्रीचे जेवण:** २ मोठ्या चपात्या, पनीर भुर्जी/मटण/चिकन आणि सॅलड.")
    else:
        st.info("**सकाळचा नाश्ता:** पोहे/उपमा/इडली आणि फळे.\n\n"
                "**दुपारचे जेवण:** २ चपात्या, थोडा भात, भाजी आणि १ वाटी ताक.\n\n"
                "**संध्याकाळचा नाश्ता:** मोड आलेले कडधान्य (Sprouts) किंवा चहा-बिस्किट.\n\n"
                "**रात्रीचे जेवण:** १ चपाती, भाजी, खिचडी आणि सॅलड.")
