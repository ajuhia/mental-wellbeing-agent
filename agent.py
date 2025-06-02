from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import re

def generate_support_plan(api_key, mental_state, sleep_pattern, stress_level, support_system, recent_changes, symptoms):
    llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.3, api_key=api_key)

    prompt_template = ChatPromptTemplate.from_template("""
You are a team of compassionate mental health buddies here to support a user through emotional challenges. 
Your job is to listen, understand, and offer guidance with warmth, encouragement, and practical help.

Based on the following information shared by the user, create a caring and thoughtful 3-part support plan:

- Emotional State: {mental_state}
- Sleep Pattern: {sleep_pattern} hours/night
- Stress Level: {stress_level}/10
- Support System: {support_system}
- Recent Life Changes: {recent_changes}
- Current Symptoms: {symptoms}

Respond using this exact format:

**1. Assessment**
(Reflect on the user's emotions and validate them.)

**2. Action Plan**
(Provide 2-4 realistic supportive actions (Do not Hallucinate) ) in list format.)

**3. Follow-Up Strategy**
(Describe long-term ideas for check-ins, self-care, or support, in list format.)

Use clear section headers exactly as shown above. No Preamle.
""")

    chain = prompt_template | llm

    response = chain.invoke({
        "mental_state": mental_state,
        "sleep_pattern": sleep_pattern,
        "stress_level": stress_level,
        "support_system": ", ".join(support_system) if support_system else "None reported",
        "recent_changes": recent_changes,
        "symptoms": ", ".join(symptoms) if symptoms else "None reported"
    })

    output_text = response.content if hasattr(response, 'content') else response
    print(" RAW LLM OUTPUT:\n", output_text)

    # Parse sections
    output = {'assessment': '', 'action': '', 'followup': ''}

    match = re.search(
        r"\*\*1\.\s*Assessment\*\*\s*(.*?)\s*\*\*2\.\s*Action Plan\*\*\s*(.*?)\s*\*\*3\.\s*Follow[- ]?Up Strategy\*\*\s*(.*)",
        output_text,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        output["assessment"] = "## What You're Going Through!\n" + match.group(1).strip()
        output["action"] = "## Support Ideas!\n" + match.group(2).strip()
        output["followup"] = "## Your Ongoing Wellness Path! \n" + match.group(3).strip()
    else:
        output["assessment"] = "The system didn’t return a valid support plan. Try providing more detailed input, or rephrasing your emotional state."

    return output
