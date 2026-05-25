from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from typing import Any, Text, Dict, List

import random

from actions.database import (
    get_micro_quiz,
    get_quiz_questions
)


class ActionHandleAnswer(Action):

    def name(self) -> Text:
        return "action_handle_answer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        user_answer = tracker.latest_message.get("text", "").strip().lower()
        micro_quiz_active = tracker.get_slot("micro_quiz_active")

        if user_answer in ["a", "option a"]:
                user_answer = "a"

        elif user_answer in ["b", "option b"]:
            user_answer = "b"

        elif user_answer in ["c", "option c"]:
         user_answer = "c"
        else:
            dispatcher.utter_message(text="Please answer using A, B, or C.")
            return []
    # HANDLE MICRO QUIZ
        if micro_quiz_active:

            topic = tracker.get_slot("micro_quiz_topic")

            quiz = get_micro_quiz(topic)

            if not quiz:

                    dispatcher.utter_message(
                        text="Micro quiz not found."
                    )

                    return []
            (
                question,
                option_a,
                option_b,
                option_c,
                correct_answer,
                explanation
            ) = quiz

            if user_answer == correct_answer.lower():

                dispatcher.utter_message(
                    text=explanation
                )

            else:

                dispatcher.utter_message(
                    text=
                    f"❌ Incorrect.\n\n"
                    f"The correct answer was {correct_answer.upper()}."
                )

            return [

                SlotSet("micro_quiz_active", False),
                SlotSet("micro_quiz_topic", None)

            ]


        questions = tracker.get_slot("quiz_questions")
        current_index = int(tracker.get_slot("current_question") or 0)
        score = int(tracker.get_slot("score") or 0)

        if not questions:
            dispatcher.utter_message(
                text="No active quiz is running right now. Type 'start quiz' to begin a new quiz or explore other Ai topics!Happy" \
                "Learning! 😊"
            )
            return []

        current_q = questions[current_index]

        if user_answer == current_q["correct_answer"].lower():
            score += 1
            dispatcher.utter_message(text="✅ Correct! Well done.")
        else:
            dispatcher.utter_message(
                    text=
                f"❌ Incorrect.\n"
                f"The correct answer was {current_q['correct_answer'].upper()}."
                )

        current_index += 1

        if current_index >= 5:
            
            if score >= 3:

                dispatcher.utter_message(
                    text=
                    f"🎉 Quiz completed!\n\n"
                    f"You scored {score}/5.\n\n"
                    "Great job! You have a strong understanding of AI concepts."
                )

            else:

                dispatcher.utter_message(
                    text=
                    f"📘 Quiz completed!\n\n"
                    f"You scored {score}/5.\n\n"
                    "You should continue exploring AI concepts to strengthen your understanding."
                )

            dispatcher.utter_message(
                text=
                "You can continue learning about:\n"
                "• AI Ethics\n"
                "• AI Bias\n"
                "• AI Risks\n"
                "• AI Regulations"
            )
            
            return [
                SlotSet("score", score),
                SlotSet("current_question", 0),
                SlotSet("quiz_questions", None)
            ]

        next_q = questions[current_index]

        next_question_text = (
                f"Question {current_index + 1}/5\n\n"
                f"{next_q['question']}\n\n"
                f"A) {next_q['option_a']}\n"
                f"B) {next_q['option_b']}\n"
                f"C) {next_q['option_c']}"
            )

        dispatcher.utter_message(text=next_question_text)

        return [
            SlotSet("current_question", current_index),
            SlotSet("score", score)
        ]

    

class ActionStartQuiz(Action):

    def name(self) -> Text:
        return "action_start_quiz"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(
        text=
        "Awesome! 🎯\n\n"
        "This quiz will test your understanding of:\n"
        "• AI Basics\n"
        "• AI Ethics\n"
        "• AI Bias\n"
        "• AI Risks\n"
        "• AI Regulations\n\n"
        "Let’s begin!"
    )
        selected_questions = get_quiz_questions()

        

        first_question = selected_questions[0]

        question_text = (
            f"Question 1/5\n\n"
            f"{first_question['question']}\n\n"
            f"A) {first_question['option_a']}\n"
            f"B) {first_question['option_b']}\n"
            f"C) {first_question['option_c']}"
            )
        

        dispatcher.utter_message(
                text="Here comes your first question 👇"
            )

        dispatcher.utter_message(text=question_text)

        
        return [
            SlotSet("quiz_questions", selected_questions),
            SlotSet("current_question", 0),
            SlotSet("score", 0)
        ]
    