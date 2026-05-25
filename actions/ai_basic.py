from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.database import (
    get_learning_content,
    get_micro_quiz,
    get_connected_topics
)

from actions.response_builder import build_learning_response


class ActionExplainTopic(Action):

    def name(self):

        return "action_explain_topic"

    def run(self, dispatcher, tracker, domain):

        # ==========================================
        # GET USER INTENT
        # ==========================================

        intent = tracker.latest_message["intent"]["name"]

        # ==========================================
        # INTENT → TOPIC MAPPING
        # ==========================================

        # topic_map = {

        #     # AI BASICS
        #     "ask_what_is_ai": "what_is_ai",
        #     "ask_history_ai": "history_ai",
        #     "ask_machine_learning": "machine_learning",
        #     "ask_supervised_learning": "supervised_learning",
        #     "ask_unsupervised_learning": "unsupervised_learning",
        #     "ask_reinforcement_learning": "reinforcement_learning",
        #     "ask_deep_learning": "deep_learning",
        #     "ask_neural_networks": "neural_networks",
        #     "ask_nlp": "nlp",
        #     "ask_computer_vision": "computer_vision",
        #     "ask_generative_ai": "generative_ai",
        #     "ask_ai_models": "ai_models",
        #     "ask_training_data": "training_data",
        #     "ask_ai_applications": "ai_applications",
        #     "ask_recommendation_systems": "recommendation_systems",
        #     "ask_chatbots": "chatbots",
        #     "ask_future_of_ai": "future_of_ai",
        #     "ask_limitations_ai": "limitations_ai",

        #     # AI IMPACT
        #     "ask_ai_healthcare": "ai_healthcare",
        #     "ask_ai_education": "ai_education",
        #     "ask_ai_finance": "ai_finance",
        #     "ask_ai_transportation": "ai_transportation",
        #     "ask_automation": "automation",
        #     "ask_job_displacement": "job_displacement",
        #     "ask_economic_impact": "economic_impact",
        #     "ask_social_impact": "social_impact",
        #     "ask_human_ai_collaboration": "human_ai_collaboration",
        #     "ask_ai_agriculture": "ai_agriculture",
        #     "ask_ai_cybersecurity": "ai_cybersecurity",
        #     "ask_ai_entertainment": "ai_entertainment",
        #     "ask_ai_productivity": "ai_productivity",
        #     "ask_ai_creativity": "ai_creativity",
        #     "ask_future_impact_ai": "future_impact_ai",

        #     # AI ETHICS
        #     "ask_fairness": "fairness",
        #     "ask_ai_ethics": "ai_ethics",
        #     "ask_accountability": "accountability",
        #     "ask_transparency": "transparency",
        #     "ask_explainable_ai": "explainable_ai",
        #     "ask_responsible_ai": "responsible_ai",
        #     "ask_ai_privacy": "ai_privacy",
        #     "ask_human_oversight": "human_oversight",
        #     "ask_trustworthy_ai": "trustworthy_ai",
        #     "ask_ai_safety": "ai_safety",
        #     "ask_ethical_decision_making": "ethical_decision_making",
        #     "ask_consent_in_ai": "consent_in_ai",
        #     "ask_ethical_ai_development": "ethical_ai_development",
        #     "ask_ai_governance_ethics": "ai_governance_ethics",
        #     "ask_moral_concerns_ai": "moral_concerns_ai",

        #     # AI BIAS
        #     "ask_data_bias": "data_bias",
        #     "ask_ai_bias": "ai_bias",
        #     "ask_algorithmic_bias": "algorithmic_bias",
        #     "ask_sampling_bias": "sampling_bias",
        #     "ask_gender_bias": "gender_bias",
        #     "ask_racial_bias": "racial_bias",
        #     "ask_hiring_bias": "hiring_bias",
        #     "ask_bias_detection": "bias_detection",
        #     "ask_reduce_bias": "reduce_bias",
        #     "ask_facial_recognition_bias": "facial_recognition_bias",
        #     "ask_bias_healthcare_ai": "bias_healthcare_ai",
        #     "ask_bias_recommendation_systems": "bias_recommendation_systems",
        #     "ask_fairness_testing": "fairness_testing",
        #     "ask_real_world_bias_examples": "real_world_bias_examples",

        #     # AI REGULATIONS
        #     "ask_ai_regulations": "ai_regulations",
        #     "ask_gdpr": "gdpr",
        #     "ask_eu_ai_act": "eu_ai_act",
        #     "ask_ai_governance": "ai_governance",
        #     "ask_compliance": "compliance",
        #     "ask_ai_auditing": "ai_auditing",
        #     "ask_ai_standards": "ai_standards",
        #     "ask_ai_accountability_laws": "ai_accountability_laws",
        #     "ask_privacy_regulations": "privacy_regulations",
        #     "ask_government_ai_policies": "government_ai_policies",
        #     "ask_international_ai_laws": "international_ai_laws",
        #     "ask_ethical_regulations": "ethical_regulations",
        #     "ask_responsible_ai_policies": "responsible_ai_policies",
        #     "ask_future_ai_regulations": "future_ai_regulations",
            

        #     # AI RISKS
        #     "ask_ai_risk": "ai_risk",
        #     "ask_misinformation": "misinformation",
        #     "ask_deepfakes": "deepfakes",
        #     "ask_privacy_risks": "privacy_risks",
        #     "ask_surveillance_risks": "surveillance_risks",
        #     "ask_cybersecurity_risks": "cybersecurity_risks",
        #     "ask_autonomous_weapons": "autonomous_weapons",
        #     "ask_ai_manipulation": "ai_manipulation",
        #     "ask_hallucinations_ai": "hallucinations_ai",
        #     "ask_overdependence_ai": "overdependence_ai",
        #     "ask_job_displacement_risk": "job_displacement_risk",
        #     "ask_social_risks": "social_risks",
        #     "ask_ethical_risks": "ethical_risks",
        #     "ask_ai_safety_risks": "ai_safety_risks",
        #     "ask_loss_human_control": "loss_human_control",
        #     "ask_future_risks_agi": "future_risks_agi"

        # }
        topic_map = {

    # =====================================================
    # AI BASICS
    # =====================================================

            "ask_what_is_ai": "what_is_ai",
            "ask_history_of_ai": "history_of_ai",
            "ask_machine_learning": "machine_learning",
            "ask_supervised_learning": "supervised_learning",
            "ask_unsupervised_learning": "unsupervised_learning",
            "ask_reinforcement_learning": "reinforcement_learning",
            "ask_deep_learning": "deep_learning",
            "ask_neural_networks": "neural_networks",
            "ask_nlp": "nlp",
            "ask_computer_vision": "computer_vision",
            "ask_generative_ai": "generative_ai",
            "ask_ai_models": "ai_models",
            "ask_training_data": "training_data",
            "ask_ai_applications": "ai_applications",
            "ask_recommendation_systems": "recommendation_systems",
            "ask_chatbots": "chatbots",
            "ask_future_of_ai": "future_of_ai",
            "ask_limitations_ai": "limitations_ai",

    # =====================================================
    # AI IMPACT
    # =====================================================
    
            "ask_ai_impact": "ai_impact",
            "ask_ai_healthcare": "ai_healthcare",
            "ask_ai_education": "ai_education",
            "ask_ai_finance": "ai_finance",
            "ask_ai_transportation": "ai_transportation",
            "ask_ai_agriculture": "ai_agriculture",
            "ask_ai_cybersecurity": "ai_cybersecurity",
            "ask_ai_entertainment": "ai_entertainment",
            "ask_ai_productivity": "ai_productivity",
            "ask_automation": "automation",
            "ask_job_displacement": "job_displacement",
            "ask_economic_impact": "economic_impact",
            "ask_social_impact": "social_impact",
            "ask_ai_creativity": "ai_creativity",
            "ask_human_ai_collaboration": "human_ai_collaboration",
            "ask_future_ai_impact": "future_impact_ai",

    # =====================================================
    # AI ETHICS
    # =====================================================

            "ask_ai_ethics": "ai_ethics",
            "ask_fairness": "fairness",
            "ask_accountability": "accountability",
            "ask_transparency": "transparency",
            "ask_explainable_ai": "explainable_ai",
            "ask_responsible_ai": "responsible_ai",
            "ask_ai_privacy": "ai_privacy",
            "ask_human_oversight": "human_oversight",
            "ask_ethical_decision_making": "ethical_decision_making",
            "ask_consent_ai": "consent_in_ai",
            "ask_trustworthy_ai": "trustworthy_ai",
            "ask_ai_safety": "ai_safety",
            "ask_ethical_ai_development": "ethical_ai_development",
            "ask_ai_governance_ethics": "ai_governance_ethics",
            "ask_moral_concerns_ai": "moral_concerns_ai",


    # =====================================================
    # AI BIAS
    # =====================================================

            "ask_ai_bias": "ai_bias",
            "ask_data_bias": "data_bias",
            "ask_algorithmic_bias": "algorithmic_bias",
            "ask_sampling_bias": "sampling_bias",
            "ask_gender_bias": "gender_bias",
            "ask_racial_bias": "racial_bias",
            "ask_hiring_bias": "hiring_bias",
            "ask_facial_recognition_bias": "facial_recognition_bias",
            "ask_healthcare_ai_bias": "bias_healthcare_ai",
            "ask_recommendation_bias": "bias_recommendation_systems",
            "ask_fairness_testing": "fairness_testing",
            "ask_reduce_bias": "reduce_bias",
            "ask_bias_detection": "bias_detection",
            "ask_bias_examples": "real_world_bias_examples",

    # =====================================================
    # AI REGULATIONS
    # =====================================================

            "ask_ai_regulations": "need_ai_regulations",
            "ask_gdpr": "gdpr",
            "ask_eu_ai_act": "eu_ai_act",
            "ask_ai_governance": "ai_governance",
            "ask_compliance": "compliance",
            "ask_ai_auditing": "ai_auditing",
            "ask_ai_accountability_laws": "ai_accountability_laws",
            "ask_privacy_regulations": "privacy_regulations",
            "ask_government_ai_policies": "government_ai_policies",
            "ask_international_ai_laws": "international_ai_laws",
            "ask_ethical_regulations": "ethical_regulations",
            "ask_ai_standards": "ai_standards",
            "ask_responsible_ai_policies": "responsible_ai_policies",
            "ask_future_ai_regulations": "future_ai_regulations",

    # =====================================================
    # AI RISKS
    # =====================================================

            "ask_ai_risk": "ai_risk",
            "ask_misinformation": "misinformation",
            "ask_deepfakes": "deepfakes",
            "ask_privacy_risks": "privacy_risks",
            "ask_surveillance_risks": "surveillance_risks",
            "ask_cybersecurity_risks": "cybersecurity_risks",
            "ask_autonomous_weapons": "autonomous_weapons",
            "ask_ai_manipulation": "ai_manipulation",
            "ask_hallucinations_ai": "hallucinations_ai",
            "ask_loss_human_control": "loss_human_control"
}

        topic_key = topic_map.get(intent)

        # ==========================================
        # INVALID TOPIC HANDLING
        # ==========================================

        if not topic_key:

            dispatcher.utter_message(
                text="I could not identify the topic."
            )

            return []

        # ==========================================
        # FETCH LEARNING CONTENT
        # ==========================================

        content = get_learning_content(topic_key)

        if not content:

            dispatcher.utter_message(
                text="Learning content not found."
            )

            return []

        # ==========================================
        # UNPACK CONTENT
        # ==========================================

        (
            title,
            definition,
            example,
            importance,
            bridge,
            reflection
        ) = content

        # ==========================================
        # BUILD RESPONSE
        # ==========================================

        response = build_learning_response(

            title,
            definition,
            example,
            importance,
            bridge,
            reflection

        )

        dispatcher.utter_message(text=response)

        # ==========================================
        # CONNECTED TOPICS
        # ==========================================

        connected_topics = get_connected_topics(topic_key)

        if connected_topics:

            next_topics = "\n".join(

                [f"• {topic.replace('_', ' ').title()}"
                 for topic in connected_topics]

            )

            dispatcher.utter_message(

                text=

                f"🔎 You may also want to explore:\n\n{next_topics}"

            )

        # ==========================================
        # MICRO QUIZ
        # ==========================================

        quiz = get_micro_quiz(topic_key)

        if quiz:

            (
                question,
                option_a,
                option_b,
                option_c,
                correct_answer,
                explanation
            ) = quiz

            dispatcher.utter_message(

                text=

                f"🧠 Quick Challenge\n\n"

                f"{question}\n\n"

                f"A) {option_a}\n"
                f"B) {option_b}\n"
                f"C) {option_c}"

            )

            return [

                SlotSet("micro_quiz_active", True),
                SlotSet("micro_quiz_answer", correct_answer),
                SlotSet("micro_quiz_topic", topic_key)

            ]

        return []