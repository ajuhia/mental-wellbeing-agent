
import streamlit as st
from agent import generate_support_plan

st.set_page_config(page_title="Mental Wellbeing Agent!!", layout="centered")

if 'output' not in st.session_state:
    st.session_state.output = {
        'assessment': '',
        'action': '',
        'followup': ''
    }

st.title(" Your Mental Wellbeing Agent")

st.info("""
**Meet Your Mental Wellbeing Support Team:** \n
**1. Assessment Agent** - Evaluates your emotional state and current needs  
**2. Action Agent** - Develops a personalized action plan and provides relevant resources  
**3. Follow-up Agent** - Generates a long-term support strategy
""")

st.subheader("Please answer the following prompts to get started:")

mental_state = st.text_area("1. How have you been feeling recently?", placeholder="Describe your emotional state, thoughts, or concerns...")
sleep_pattern = st.select_slider("2. Sleep Pattern (hours per night)", options=[f"{i}" for i in range(0, 13)], value="7")
stress_level = st.slider("3. Current Stress Level (1-10)", 1, 10, 5)
support_system = st.multiselect("4. Current Support System", ["Family", "Friends", "Therapist", "Medications", "Support Groups", "None"])
recent_changes = st.text_area("5. Any significant recent life changes/events?", placeholder="Job changes, relationships, losses, etc...")
current_symptoms = st.multiselect("6. Current Symptoms", [
     "Loss of Interest", "Anxiety", "Depressed Mood", "Sleep Issues", "Fatigue",
    "Trouble Concentrating", "Changes in Appetite", "Social Withdrawal",
    "Feelings of Failure", "Sucidal Thoughts", "Psychomotor Changes"])

if st.button("Generate Support Plan"):
    if not mental_state or not recent_changes or not current_symptoms:
        st.warning("Please fill in all required fields before generating the plan.")
    else:
        with st.spinner('🤖 AI Agents are analyzing your situation...'):
            try:
                output = generate_support_plan(
                    api_key=None,
                    mental_state=mental_state,
                    sleep_pattern=sleep_pattern,
                    stress_level=stress_level,
                    support_system=support_system,
                    recent_changes=recent_changes,
                    symptoms=current_symptoms
                )
                #st.write("DEBUG Output:", output)
                st.session_state.output = output

                st.markdown("### Your Personalized Mental Health Support Plan")
                st.markdown(st.session_state.output['assessment'])
                st.markdown(st.session_state.output['action'])
                st.markdown(st.session_state.output['followup'])
                st.success(" Mental health support plan generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.warning("🚨 If you're in crisis, contact 911 emergency service.")

