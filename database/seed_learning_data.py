# COMPLETE `seed_learning_data.py`

import sqlite3


# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("database/ai_compass.db")

cursor = conn.cursor()


# ==========================================
# INSERT MODULES
# ==========================================

modules = [

    ("AI Basics",),
    ("AI Impact",),
    ("AI Ethics",),
    ("AI Bias",),
    ("AI Regulations",),
    ("AI Risks",)

]

cursor.executemany("""

INSERT OR IGNORE INTO modules (module_name)

VALUES (?)

""", modules)


# ==========================================
# GET MODULE IDS
# ==========================================

module_ids = {}

cursor.execute("SELECT id, module_name FROM modules")

for row in cursor.fetchall():
    module_ids[row[1]] = row[0]


# ==========================================
# TOPICS
# ==========================================

topics = [

    # =====================================================
    # AI BASICS
    # =====================================================

    (module_ids["AI Basics"], "what_is_ai", "What is AI"),
    (module_ids["AI Basics"], "history_of_ai", "History of AI"),
    (module_ids["AI Basics"], "machine_learning", "Machine Learning"),
    (module_ids["AI Basics"], "supervised_learning", "Supervised Learning"),
    (module_ids["AI Basics"], "unsupervised_learning", "Unsupervised Learning"),
    (module_ids["AI Basics"], "reinforcement_learning", "Reinforcement Learning"),
    (module_ids["AI Basics"], "deep_learning", "Deep Learning"),
    (module_ids["AI Basics"], "neural_networks", "Neural Networks"),
    (module_ids["AI Basics"], "nlp", "Natural Language Processing"),
    (module_ids["AI Basics"], "computer_vision", "Computer Vision"),
    (module_ids["AI Basics"], "generative_ai", "Generative AI"),
    (module_ids["AI Basics"], "ai_models", "AI Models"),
    (module_ids["AI Basics"], "training_data", "Training Data"),
    (module_ids["AI Basics"], "ai_applications", "AI Applications"),
    (module_ids["AI Basics"], "recommendation_systems", "Recommendation Systems"),
    (module_ids["AI Basics"], "chatbots", "Chatbots"),
    (module_ids["AI Basics"], "future_of_ai", "Future of AI"),
    (module_ids["AI Basics"], "limitations_ai", "Limitations of AI"),


    # =====================================================
    # AI IMPACT
    # =====================================================
    (module_ids["AI Impact"], "ai_impact", "Impact of AI"),
    (module_ids["AI Impact"], "ai_healthcare", "AI in Healthcare"),
    (module_ids["AI Impact"], "ai_education", "AI in Education"),
    (module_ids["AI Impact"], "ai_finance", "AI in Finance"),
    (module_ids["AI Impact"], "ai_transportation", "AI in Transportation"),
    (module_ids["AI Impact"], "automation", "Automation"),
    (module_ids["AI Impact"], "job_displacement", "Job Displacement"),
    (module_ids["AI Impact"], "economic_impact", "Economic Impact"),
    (module_ids["AI Impact"], "social_impact", "Social Impact"),
    (module_ids["AI Impact"], "human_ai_collaboration", "Human-AI Collaboration"),
    (module_ids["AI Impact"], "ai_agriculture", "AI in Agriculture"),
    (module_ids["AI Impact"], "ai_cybersecurity", "AI in Cybersecurity"),
    (module_ids["AI Impact"], "ai_entertainment", "AI in Entertainment"),
    (module_ids["AI Impact"], "ai_productivity", "AI and Productivity"),
    (module_ids["AI Impact"], "ai_creativity", "AI and Creativity"),
    (module_ids["AI Impact"], "future_impact_ai", "Future Impact of AI"),


    # =====================================================
    # AI ETHICS
    # =====================================================

    (module_ids["AI Ethics"], "fairness", "Fairness"),
    (module_ids["AI Ethics"], "ai_ethics", "AI Ethics"),
    (module_ids["AI Ethics"], "accountability", "Accountability"),
    (module_ids["AI Ethics"], "transparency", "Transparency"),
    (module_ids["AI Ethics"], "explainable_ai", "Explainable AI"),
    (module_ids["AI Ethics"], "responsible_ai", "Responsible AI"),
    (module_ids["AI Ethics"], "ai_privacy", "AI Privacy"),
    (module_ids["AI Ethics"], "human_oversight", "Human Oversight"),
    (module_ids["AI Ethics"], "trustworthy_ai", "Trustworthy AI"),
    (module_ids["AI Ethics"], "ai_safety", "AI Safety"),
    (module_ids["AI Ethics"], "ethical_decision_making", "Ethical Decision Making"),
    (module_ids["AI Ethics"], "consent_in_ai", "Consent in AI"),
    (module_ids["AI Ethics"], "ethical_ai_development", "Ethical AI Development"),
    (module_ids["AI Ethics"], "ai_governance_ethics", "AI Governance and Ethics"),
    (module_ids["AI Ethics"], "moral_concerns_ai", "Moral Concerns in AI"),



    # =====================================================
    # AI BIAS
    # =====================================================

    (module_ids["AI Bias"], "data_bias", "Data Bias"),
    (module_ids["AI Bias"], "ai_bias", "AI Bias"),
    (module_ids["AI Bias"], "algorithmic_bias", "Algorithmic Bias"),
    (module_ids["AI Bias"], "sampling_bias", "Sampling Bias"),
    (module_ids["AI Bias"], "gender_bias", "Gender Bias"),
    (module_ids["AI Bias"], "racial_bias", "Racial Bias"),
    (module_ids["AI Bias"], "hiring_bias", "Hiring Bias"),
    (module_ids["AI Bias"], "bias_detection", "Bias Detection"),
    (module_ids["AI Bias"], "reduce_bias", "Reducing AI Bias"),
    (module_ids["AI Bias"], "facial_recognition_bias", "Facial Recognition Bias"),
    (module_ids["AI Bias"], "bias_healthcare_ai", "Bias in Healthcare AI"),
    (module_ids["AI Bias"], "bias_recommendation_systems", "Bias in Recommendation Systems"),
    (module_ids["AI Bias"], "fairness_testing", "Fairness Testing"),
    (module_ids["AI Bias"], "real_world_bias_examples", "Real-world AI Bias Examples"),

    # =====================================================
    # AI REGULATIONS
    # =====================================================
    (module_ids["AI Regulations"], "need_ai_regulations", "Why We Need AI Regulations"),
    (module_ids["AI Regulations"], "gdpr", "GDPR"),
    (module_ids["AI Regulations"], "eu_ai_act", "EU AI Act"),
    (module_ids["AI Regulations"], "ai_governance", "AI Governance"),
    (module_ids["AI Regulations"], "compliance", "Compliance"),
    (module_ids["AI Regulations"], "ai_auditing", "AI Auditing"),
    (module_ids["AI Regulations"], "ai_standards", "AI Standards"),
    (module_ids["AI Regulations"], "ai_accountability_laws", "AI Accountability Laws"),
    (module_ids["AI Regulations"], "privacy_regulations", "Privacy Regulations"),
    (module_ids["AI Regulations"], "government_ai_policies", "Government AI Policies"),
    (module_ids["AI Regulations"], "international_ai_laws", "International AI Laws"),
    (module_ids["AI Regulations"], "ai_regulatory_bodies", "AI Regulatory Bodies"),
    (module_ids["AI Regulations"], "ai_regulation_challenges", "Challenges in AI Regulations"),
    (module_ids["AI Regulations"], "future_ai_regulations", "Future of AI Regulations"),




    # =====================================================
    # AI RISKS
    # =====================================================
    
    (module_ids["AI Risks"], "ai_risk", "AI Risks"),
    (module_ids["AI Risks"], "misinformation", "Misinformation"),
    (module_ids["AI Risks"], "deepfakes", "Deepfakes"),
    (module_ids["AI Risks"], "privacy_risks", "Privacy Risks"),
    (module_ids["AI Risks"], "surveillance_risks", "Surveillance Risks"),
    (module_ids["AI Risks"], "cybersecurity_risks", "Cybersecurity Risks"),
    (module_ids["AI Risks"], "autonomous_weapons", "Autonomous Weapons"),
    (module_ids["AI Risks"], "ai_manipulation", "AI Manipulation"),
    (module_ids["AI Risks"], "hallucinations_ai", "Hallucinations in AI"),
    (module_ids["AI Risks"], "overdependence_ai", "Overdependence on AI"),
    (module_ids["AI Risks"], "job_displacement_risk", "Job Displacement Risk"),
    (module_ids["AI Risks"], "social_risks", "Social Risks"),
    (module_ids["AI Risks"], "ethical_risks", "Ethical Risks"),
    (module_ids["AI Risks"], "ai_safety_risks", "AI Safety Risks"),
    (module_ids["AI Risks"], "loss_human_control", "Loss of Human Control"),
    (module_ids["AI Risks"], "future_risks_agi", "Future Risks of AGI")

]

cursor.executemany("""

INSERT OR REPLACE INTO topics (

    module_id,
    topic_key,
    title

)

VALUES (?, ?, ?)

""", topics)


# Expanded `learning_content`, `micro_quizzes`, and `connections`

# ==========================================
# LEARNING CONTENT
# ==========================================

learning_content = [

    # =====================================================
    # AI BASICS
    # =====================================================

    (
        "what_is_ai",
        "Artificial Intelligence refers to computer systems designed to perform tasks that normally require human intelligence.",
        "Voice assistants like Siri and Google Assistant use AI to understand and answer questions.",
        "AI is transforming industries by automating tasks and improving decision-making.",
        "AI is built using concepts like Machine Learning, Neural Networks, and Deep Learning.",
        "Which daily activities around you already depend on AI?"
    ),

    (
        "history_of_ai",

        "The History of AI explores how artificial intelligence evolved from early mathematical theories into modern intelligent systems.",

        "Early AI systems in the 1950s could solve basic mathematical and logical problems.",

        "Understanding AI history helps explain how modern technologies like ChatGPT and self-driving cars became possible.",

        "AI development accelerated with improvements in computing power, data availability, and Machine Learning.",

        "Why do technological advances often accelerate AI progress?"
    ),

    (
        "ai_models",

        "AI Models are trained systems that learn patterns from data to make predictions or decisions.",

        "Recommendation systems use AI models to predict what users may want to watch or buy.",

        "AI models are the core engines behind intelligent systems like chatbots, image recognition, and search engines.",

        "Different AI models are designed for tasks such as language processing, image analysis, and prediction.",

        "Why might different AI problems require different types of models?"
    ),

    (
        "training_data",

        "Training Data is the information used to teach AI systems how to recognize patterns and make decisions.",

        "Medical AI systems learn by analyzing thousands of medical scans and patient records.",

        "The quality and diversity of training data strongly affect AI accuracy and fairness.",

        "Biased or incomplete training data can create unfair AI systems.",

        "Why can poor training data create dangerous AI outcomes?"
    ),

    (
        "ai_applications",

        "AI Applications are real-world uses of AI across industries, businesses, and daily life.",

        "AI powers recommendation systems, fraud detection, virtual assistants, and healthcare diagnostics.",

        "AI applications improve efficiency, automation, personalization, and decision-making.",

        "AI is rapidly expanding into education, transportation, cybersecurity, and entertainment.",

        "Which industries around you are being transformed most by AI?"
    ),

    (
        "recommendation_systems",

        "Recommendation Systems predict what users may like based on behavior, preferences, and past interactions.",

        "Spotify recommends songs by analyzing listening habits and user preferences.",

        "These systems improve personalization and user engagement across digital platforms.",

        "Recommendation systems rely heavily on Machine Learning and user data analysis.",

        "Why can recommendation systems sometimes create filter bubbles or echo chambers?"
    ),


    (
        "limitations_ai",

        "Limitations of AI include bias, lack of common sense, dependence on data, and difficulty understanding human emotions fully.",

        "AI chatbots can sometimes generate incorrect information confidently.",

        "Understanding AI limitations helps humans use AI responsibly and avoid overdependence.",

        "AI limitations are closely connected to AI risks, ethics, and safety concerns.",

        "Why should humans verify important AI-generated decisions?"
    ),

    (
        "machine_learning",
        "Machine Learning enables systems to learn patterns from data without explicit programming.",
        "Netflix recommendations use Machine Learning to suggest movies.",
        "Machine Learning powers prediction systems, automation, and personalization.",
        "Machine Learning includes supervised, unsupervised, and reinforcement learning.",
        "Why does Machine Learning depend heavily on quality data?"
    ),

    (
        "supervised_learning",
        "Supervised Learning trains AI models using labeled datasets.",
        "Email spam filters learn from examples marked as spam or not spam.",
        "It is widely used for prediction and classification tasks.",
        "Supervised Learning is one of the main branches of Machine Learning.",
        "Why are labeled datasets important in supervised learning?"
    ),

    (
        "unsupervised_learning",
        "Unsupervised Learning identifies hidden patterns in unlabeled data.",
        "Customer segmentation systems group users with similar behavior.",
        "It helps discover structures and relationships humans may miss.",
        "Clustering and anomaly detection are common unsupervised techniques.",
        "How can AI discover useful patterns without labels?"
    ),

    (
        "reinforcement_learning",
        "Reinforcement Learning teaches AI systems through rewards and penalties.",
        "Game-playing AI improves by receiving rewards for successful actions.",
        "It enables AI to optimize long-term decision-making.",
        "Reinforcement Learning is used in robotics and autonomous systems.",
        "Why might reward systems influence AI behavior strongly?"
    ),

    (
        "deep_learning",
        "Deep Learning uses multi-layered neural networks to process complex data.",
        "Facial recognition systems rely on Deep Learning models.",
        "Deep Learning powers speech recognition, translation, and Generative AI.",
        "Deep Learning models are built using Neural Networks.",
        "Why do deeper networks often improve recognition accuracy?"
    ),

    (
        "neural_networks",
        "Neural Networks are AI systems inspired by interconnected neurons in the human brain.",
        "Image recognition AI uses Neural Networks to identify objects.",
        "They form the foundation of many modern AI breakthroughs.",
        "Deep Learning depends heavily on Neural Networks.",
        "Why are layered neural structures useful for AI learning?"
    ),

    (
        "nlp",
        "Natural Language Processing enables AI systems to understand and generate human language.",
        "Chatbots use NLP to answer customer questions.",
        "NLP improves communication between humans and machines.",
        "Large Language Models are advanced NLP systems.",
        "How does language ambiguity make NLP difficult?"
    ),

    (
        "computer_vision",
        "Computer Vision enables machines to interpret and analyze images and videos.",
        "Self-driving cars use Computer Vision to detect roads and pedestrians.",
        "It allows AI systems to interact with the visual world.",
        "Computer Vision often relies on Deep Learning models.",
        "Why is image recognition harder than simple text matching?"
    ),

    (
        "generative_ai",
        "Generative AI creates new content such as text, images, music, or videos.",
        "AI image generators can create realistic artwork from prompts.",
        "Generative AI is transforming creativity, productivity, and entertainment.",
        "Generative AI systems are often trained using Deep Learning.",
        "What risks arise when AI can generate realistic content?"
    ),

    (
        "ai_models",
        "AI Models are trained systems that make predictions or decisions from data.",
        "Recommendation engines use AI models to predict user interests.",
        "AI models are the operational core of intelligent systems.",
        "Different models are designed for different AI tasks.",
        "Why might one AI model perform better than another?"
    ),

    (
        "training_data",
        "Training Data is the dataset used to teach AI systems patterns and relationships.",
        "Medical AI systems train on thousands of medical scans.",
        "The quality of training data strongly affects AI performance.",
        "Poor training data can introduce AI bias.",
        "Why can biased data create unfair AI outcomes?"
    ),

    (
        "ai_applications",
        "AI Applications are practical uses of AI across industries and daily life.",
        "AI powers fraud detection, recommendation systems, and virtual assistants.",
        "AI applications improve efficiency, accuracy, and automation.",
        "Many industries are integrating AI into existing systems.",
        "Which industry around you is being transformed most by AI?"
    ),

    (
        "recommendation_systems",
        "Recommendation Systems predict what users may like or need.",
        "Spotify recommends songs based on listening behavior.",
        "These systems increase user engagement and personalization.",
        "Recommendation systems rely heavily on Machine Learning.",
        "Why can recommendation systems sometimes create echo chambers?"
    ),

    (
        "chatbots",
        "Chatbots are AI systems designed to simulate conversations with humans.",
        "Customer support bots answer user questions automatically.",
        "Chatbots improve support availability and reduce workload.",
        "Modern chatbots rely on NLP and Generative AI.",
        "Why do some chatbots struggle with complex conversations?"
    ),

    (
        "future_of_ai",
        "The Future of AI explores how intelligent systems may evolve and impact society.",
        "AI may assist scientists in discovering new medicines faster.",
        "Understanding AI's future helps societies prepare responsibly.",
        "Future AI development raises ethical and regulatory concerns.",
        "Should AI development have global limits or controls?"
    ),

    (
        "limitations_ai",
        "Limitations of AI include bias, lack of common sense, and dependence on data.",
        "AI chatbots sometimes generate incorrect information confidently.",
        "Recognizing AI limitations prevents overdependence on technology.",
        "AI limitations connect closely with AI risks and ethics.",
        "Why should humans verify important AI-generated decisions?"
    ),


    # =====================================================
    # AI IMPACT
    # =====================================================

    (
        "ai_impact",
        
        "AI Impact refers to the influence Artificial Intelligence has on industries, jobs, society, and everyday life.",
        "AI is used in healthcare, finance, education, transportation, and entertainment to improve efficiency and decision-making.",
        "Understanding AI impact helps society prepare for both opportunities and risks created by AI technologies.",
        "AI impact can be economic, social, ethical, and technological.",
        "How might AI change the way humans work and live in the future?"
    ),

    (
        "ai_healthcare",

        "AI in Healthcare helps doctors and medical professionals analyze diseases, patient data, and treatment options more efficiently.",

        "AI systems can detect tumors in medical scans and assist doctors in diagnosing diseases earlier.",

        "Healthcare AI can improve diagnosis accuracy, reduce workload, and help patients receive faster treatment.",

        "Healthcare AI also raises important questions about privacy, ethics, and human oversight.",

        "Should AI systems ever make medical decisions without human doctors?"
    ),

    (
        "ai_education",

        "AI in Education personalizes learning experiences based on each student's needs and progress.",

        "Online learning platforms can recommend lessons and exercises based on student performance.",

        "AI can improve accessibility, automate repetitive tasks, and support both students and teachers.",

        "Educational AI systems rely heavily on learning analytics and student data.",

        "Can AI fully replace human teachers in the future?"
    ),

    (
        "ai_finance",

        "AI in Finance helps analyze transactions, detect fraud, assess risks, and automate financial operations.",

        "Banks use AI systems to identify suspicious transactions and prevent fraud in real time.",

        "AI improves speed, accuracy, and efficiency in financial decision-making.",

        "Financial AI systems must remain transparent, secure, and fair to customers.",

        "How could biased financial AI systems negatively affect people?"
    ),

    (
        "ai_transportation",

        "AI in Transportation improves navigation, automation, traffic management, and road safety.",

        "Self-driving cars use AI to understand road conditions and avoid obstacles.",

        "Transportation AI can reduce accidents, improve efficiency, and lower traffic congestion.",

        "Autonomous transportation systems rely heavily on Computer Vision and real-time decision-making.",

        "What risks could occur if transportation AI systems make incorrect decisions?"
    ),

    (
        "automation",

        "Automation uses AI and technology to perform repetitive or routine tasks automatically.",

        "Factories use robotic systems to automate manufacturing and assembly processes.",

        "Automation increases productivity, efficiency, and operational speed across industries.",

        "Automation can also contribute to workforce disruption and job displacement.",

        "Which types of jobs are most vulnerable to automation?"
    ),

    (
        "job_displacement",

        "Job Displacement happens when AI and automation replace certain human job roles.",

        "Customer support chatbots can automate repetitive service tasks previously done by humans.",

        "Understanding job displacement helps societies prepare workers for technological change.",

        "At the same time, AI is also creating new careers and technical job opportunities.",

        "How should governments and companies prepare workers for AI-driven changes?"
    ),

    (
        "economic_impact",

        "Economic Impact of AI refers to how AI changes industries, productivity, businesses, and employment.",

        "Companies use AI to reduce costs, improve efficiency, and increase profits.",

        "AI could significantly boost economic growth while also increasing inequality risks.",

        "The long-term economic impact of AI depends on responsible and balanced adoption.",

        "Who is likely to benefit most economically from advanced AI technologies?"
    ),

    (
        "social_impact",

        "Social Impact of AI refers to how AI changes communication, relationships, behavior, and society.",

        "Social media recommendation algorithms influence what millions of users see online every day.",

        "AI can shape public opinion, influence behavior, and affect trust in information.",

        "The social impact of AI is closely connected to misinformation and ethical concerns.",

        "How does AI influence the way people interact and consume information online?"
    ),

    (
        "human_ai_collaboration",

        "Human-AI Collaboration combines human judgment and creativity with AI speed and analytical abilities.",

        "Doctors use AI tools to assist with medical diagnosis while still making final decisions themselves.",

        "Collaboration allows humans and AI systems to work together more effectively.",

        "Human oversight remains essential in high-risk AI-assisted systems.",

        "Why should humans remain involved in important AI decisions?"
    ),

    (
        "ai_agriculture",

        "AI in Agriculture helps farmers improve crop monitoring, irrigation, and disease detection.",

        "AI-powered drones can analyze farmland and identify unhealthy crops early.",

        "Agricultural AI can improve food production and reduce resource waste.",

        "AI agriculture systems rely on sensors, data analysis, and predictive models.",

        "How could AI help address future food shortages?"
    ),

    (
        "ai_cybersecurity",

        "AI in Cybersecurity helps detect threats, monitor suspicious activity, and respond to cyberattacks quickly.",

        "Security systems use AI to identify unusual network behavior that may indicate hacking attempts.",

        "AI improves the speed and accuracy of cybersecurity defenses.",

        "Cybersecurity AI must also defend against AI-powered attacks and manipulation.",

        "Can AI systems themselves become targets for cyberattacks?"
    ),

    (
        "ai_entertainment",

        "AI in Entertainment helps create personalized content, recommendations, and digital media experiences.",

        "Streaming platforms use AI to recommend movies, music, and shows to users.",

        "Entertainment AI increases personalization and user engagement.",

        "Generative AI is increasingly being used to create music, images, videos, and scripts.",

        "How might AI change the future of movies, music, and gaming?"
    ),

    (
        "ai_productivity",

        "AI and Productivity refers to how AI helps people complete tasks faster and more efficiently.",

        "AI assistants can summarize documents, organize schedules, and automate repetitive work.",

        "AI productivity tools can save time and improve decision-making.",

        "Overdependence on AI tools may also reduce certain human skills over time.",

        "Which human skills will remain important even as AI productivity tools improve?"
    ),

    (
        "ai_creativity",

        "AI and Creativity explores how AI systems can assist in generating art, music, writing, and design.",

        "Generative AI tools can create digital artwork, poems, and music compositions.",

        "AI creativity is changing how people create and interact with digital content.",

        "Human creativity and AI generation are increasingly working together.",

        "Can AI truly be creative, or is it only recombining human-created patterns?"
    ),

    (
        "future_impact_ai",

        "Future Impact of AI refers to how advanced AI systems may reshape society, industries, and human life in the coming decades.",

        "Future AI could transform healthcare, transportation, education, scientific research, and communication.",

        "The long-term impact of AI may bring both major opportunities and serious risks.",

        "Future AI development raises important questions about ethics, governance, and human control.",

        "How should humanity prepare for increasingly powerful AI systems?"
    ),

    # =====================================================
    # AI ETHICS
    # =====================================================

    (
        "fairness",

        "Fairness in AI means ensuring AI systems treat individuals and groups equally without unfair discrimination.",

        "A hiring AI system should evaluate candidates based on skills and qualifications rather than gender or background.",

        "Fair AI systems help build trust and reduce harmful bias in automated decision-making.",

        "Fairness is closely connected to bias detection, responsible AI, and accountability.",

        "How can unfair training data affect fairness in AI systems?"
    ),

    (
        "ai_ethics",

        "AI Ethics is the study of moral principles and responsibilities involved in designing and using AI systems.",

        "Companies developing AI systems must consider how their technology affects people and society.",

        "AI Ethics helps ensure AI is used safely, fairly, and responsibly.",

        "Important areas of AI Ethics include fairness, transparency, privacy, accountability, and safety.",

        "Should governments create strict laws to regulate AI ethics?"
    ),

    (
        "accountability",

        "Accountability in AI means humans and organizations remain responsible for the decisions and impacts of AI systems.",

        "If an AI system causes harm, the company that created or deployed it may still be legally responsible.",

        "Accountability prevents organizations from avoiding responsibility for harmful AI outcomes.",

        "AI governance and regulations often require accountability mechanisms.",

        "Who should be responsible when AI systems make harmful mistakes?"
    ),

    (
        "transparency",

        "Transparency means AI systems should clearly explain how important decisions are made.",

        "A bank using AI for loan approval may explain why an application was accepted or rejected.",

        "Transparent AI systems help users understand and trust automated decisions.",

        "Explainable AI is an important part of transparency.",

        "Why might people distrust AI systems that hide their decision-making process?"
    ),

    (
        "explainable_ai",

        "Explainable AI focuses on making AI decisions understandable and interpretable for humans.",

        "Doctors may require explanations from medical AI systems before trusting a diagnosis.",

        "Explainability improves trust, safety, and accountability in AI systems.",

        "Complex Deep Learning models are often difficult to fully explain.",

        "Why can black-box AI systems become risky in critical industries like healthcare?"
    ),

    (
        "responsible_ai",

        "Responsible AI means designing and using AI systems in ways that are ethical, safe, fair, and beneficial to society.",

        "Companies may test AI systems for bias and safety before releasing them publicly.",

        "Responsible AI helps reduce harm and improve public trust in technology.",

        "Responsible AI combines fairness, transparency, privacy, and human oversight.",

        "Should responsible AI practices become mandatory for all companies?"
    ),

    (
        "ai_privacy",

        "AI Privacy focuses on protecting personal and sensitive information used by AI systems.",

        "Apps collecting user behavior data must securely handle personal information.",

        "Strong privacy protection helps prevent misuse of personal data and surveillance risks.",

        "Privacy laws such as GDPR regulate how organizations use and store data.",

        "Why should users have control over how their personal data is used?"
    ),

    (
        "human_oversight",

        "Human Oversight means humans remain involved in monitoring and controlling important AI decisions.",

        "Autonomous vehicles may still require human intervention during emergencies.",

        "Human oversight helps prevent unsafe or harmful AI behavior.",

        "Critical AI systems should not operate without supervision or review.",

        "What risks could arise if AI systems operated completely independently?"
    ),

    (
        "trustworthy_ai",

        "Trustworthy AI refers to AI systems that are reliable, ethical, transparent, and safe to use.",

        "Healthcare AI systems must provide dependable and accurate results to gain public trust.",

        "Trustworthy AI increases confidence and encourages responsible AI adoption.",

        "Trust in AI depends on fairness, accountability, transparency, and safety.",

        "Why is public trust important for the future adoption of AI technologies?"
    ),

    (
        "ai_safety",

        "AI Safety focuses on preventing AI systems from causing harm or behaving unpredictably.",

        "Self-driving cars must avoid making unsafe decisions that could endanger people.",

        "AI safety is especially important in healthcare, transportation, and autonomous systems.",

        "Safety concerns become more serious as AI systems grow more powerful and autonomous.",

        "How can societies ensure advanced AI systems remain safe and controllable?"
    ),

    (
        "ethical_decision_making",

        "Ethical Decision Making in AI involves ensuring AI systems make choices that align with human values and moral principles.",

        "Self-driving cars may face situations where AI must choose between multiple risky outcomes during accidents.",

        "Ethical decision-making helps reduce harm and improves trust in advanced AI systems.",

        "AI Ethics and Human Oversight both play important roles in ethical AI decisions.",

        "Should AI systems ever be allowed to make life-and-death decisions independently?"
    ),

    (
        "consent_in_ai",

        "Consent in AI means users should understand and agree to how their data is collected and used by AI systems.",

        "Social media platforms often request permission before collecting user activity data.",

        "Proper consent helps protect privacy and gives users more control over personal information.",

        "Privacy laws like GDPR emphasize the importance of informed consent.",

        "Do people always fully understand what they agree to when accepting data policies?"
    ),

    (
        "ethical_ai_development",

        "Ethical AI Development focuses on building AI systems that are fair, safe, transparent, and beneficial to society.",

        "Companies may create internal ethical guidelines before launching AI products.",

        "Ethical development helps prevent harmful AI behavior and improves public trust.",

        "Responsible AI practices are an important part of ethical AI development.",

        "Should ethical reviews become mandatory before releasing advanced AI systems?"
    ),

    (
        "ai_governance_ethics",

        "AI Governance Ethics focuses on creating rules, policies, and oversight mechanisms for responsible AI use.",

        "Governments and organizations may establish ethical standards for AI deployment.",

        "Strong governance helps ensure AI systems remain fair, accountable, and safe.",

        "AI Governance combines ethics, regulation, accountability, and safety practices.",

        "Who should decide the ethical boundaries for powerful AI systems?"
    ),

    (
        "moral_concerns_ai",

        "Moral Concerns in AI refer to ethical questions about how AI systems affect human rights, society, and decision-making.",

        "People worry about issues such as surveillance, job displacement, manipulation, and loss of human control.",

        "Understanding moral concerns helps societies use AI responsibly and thoughtfully.",

        "Advanced AI systems raise new ethical and philosophical challenges for humanity.",

        "How should societies balance AI innovation with ethical responsibility?"
    ),


    # =====================================================
    # AI BIAS
    # =====================================================

    (
        "data_bias",

        "Data Bias happens when the data used to train AI does not fairly represent real-world populations or situations.",

        "Facial recognition systems may perform poorly on certain groups if those groups were underrepresented in the training data.",

        "Biased data can lead to unfair AI decisions and reduce trust in AI systems.",

        "Bias detection and fairness testing help identify problems in training data.",

        "Why is it dangerous when AI learns from incomplete or unbalanced data?"
    ),

    (
        "ai_bias",

        "AI Bias refers to unfair or systematic errors in AI systems that can disadvantage certain individuals or groups.",

        "A hiring AI may unfairly favor certain candidates because of patterns learned from historical hiring data.",

        "Understanding AI Bias is important for building fair, trustworthy, and responsible AI systems.",

        "Bias can appear in datasets, algorithms, or even how AI systems are deployed.",

        "Can AI systems ever become completely free from bias?"
    ),

    (
        "algorithmic_bias",

        "Algorithmic Bias occurs when the logic or design of an AI system produces unfair outcomes.",

        "A loan approval system may unfairly reject applications from certain communities because of biased decision patterns.",

        "Algorithmic bias can reinforce social inequality and reduce fairness in automated decision-making.",

        "Bias may come from both training data and the way algorithms are designed.",

        "Why should developers regularly test AI systems for unfair behavior?"
    ),

    (
        "sampling_bias",

        "Sampling Bias happens when collected data does not properly represent the full population.",

        "If a survey only includes responses from one age group, the results may become misleading.",

        "Sampling bias reduces AI accuracy and can create unfair predictions.",

        "Balanced and diverse datasets improve AI reliability.",

        "Why might small or limited datasets increase bias in AI systems?"
    ),

    (
        "gender_bias",

        "Gender Bias occurs when AI systems unfairly favor or disadvantage people based on gender.",

        "A recruitment AI trained on historical hiring records may unintentionally prefer male applicants.",

        "Reducing gender bias helps create fairer workplaces and AI systems.",

        "Historical data can unintentionally teach AI systems biased patterns.",

        "How can past human decisions influence modern AI systems?"
    ),

    (
        "racial_bias",

        "Racial Bias occurs when AI systems produce unfair outcomes for people from different racial or ethnic groups.",

        "Some facial recognition systems have shown higher error rates for underrepresented racial groups.",

        "Racial bias can damage trust and create serious social and legal concerns.",

        "Fairness testing helps developers identify and reduce racial bias in AI systems.",

        "Why is fairness especially important in law enforcement AI systems?"
    ),

    (
        "hiring_bias",

        "Hiring Bias happens when recruitment AI unfairly favors or rejects certain candidates.",

        "An AI resume screening system may prefer applicants who resemble previously hired employees.",

        "Biased hiring systems can reduce diversity and create unfair opportunities.",

        "Responsible AI practices include regular auditing of recruitment systems.",

        "Should companies always explain how hiring AI makes decisions?"
    ),

    (
        "bias_detection",

        "Bias Detection involves identifying unfair patterns or unequal treatment in AI systems.",

        "Developers may test whether an AI system behaves differently across demographic groups.",

        "Bias detection helps organizations build safer and fairer AI technologies.",

        "Bias testing is an important part of responsible AI development.",

        "Why should AI systems be tested before being deployed publicly?"
    ),

    (
        "reduce_bias",

        "Reducing AI Bias involves improving datasets, algorithms, and evaluation methods to create fairer AI systems.",

        "Developers may use more diverse training data to reduce discrimination in AI predictions.",

        "Reducing bias improves fairness, reliability, and public trust in AI systems.",

        "Fairness testing and human oversight both support bias reduction efforts.",

        "Can humans themselves introduce bias while trying to reduce AI bias?"
    ),

    (
        "facial_recognition_bias",

        "Facial Recognition Bias occurs when facial recognition systems perform unevenly across different demographic groups.",

        "Some facial recognition systems have shown higher error rates for women and people with darker skin tones.",

        "Biased facial recognition systems can lead to discrimination, false identification, and legal concerns.",

        "Improving training data diversity helps reduce facial recognition bias.",

        "Why can inaccurate facial recognition systems become dangerous in public surveillance?"
    ),

    (
        "bias_healthcare_ai",

        "Bias in Healthcare AI happens when medical AI systems produce unfair or inaccurate outcomes for certain patient groups.",

        "An AI diagnosis system trained mostly on data from one population may perform poorly for other groups.",

        "Healthcare bias can affect treatment quality, diagnosis accuracy, and patient safety.",

        "Medical AI systems require diverse and carefully tested datasets.",

        "Why is fairness especially important in healthcare-related AI systems?"
    ),

    (
        "bias_recommendation_systems",

        "Bias in Recommendation Systems occurs when AI repeatedly promotes limited or unfair content patterns.",

        "Video platforms may continuously recommend extreme or repetitive content to increase engagement.",

        "Biased recommendations can influence opinions, behavior, and information exposure.",

        "Recommendation systems rely heavily on user behavior and Machine Learning models.",

        "How can recommendation systems unintentionally create echo chambers?"
    ),

    (
        "fairness_testing",

        "Fairness Testing evaluates whether AI systems treat different individuals and groups fairly.",

        "Developers may compare how an AI hiring system behaves across genders or demographic groups.",

        "Fairness testing helps organizations identify hidden bias before AI systems are deployed.",

        "Bias detection and auditing are important parts of fairness testing.",

        "Should fairness testing become mandatory for high-risk AI systems?"
    ),

    (
        "real_world_bias_examples",

        "Real-world AI Bias examples show how unfair AI systems can affect society and decision-making.",

        "Some hiring AI systems have unfairly favored certain applicants because of biased historical hiring data.",

        "Studying real-world bias helps developers build safer and more responsible AI systems.",

        "Bias can appear in hiring, healthcare, policing, finance, and recommendation systems.",

        "What lessons can society learn from past AI bias failures?"
    ),

    # =====================================================
    # AI REGULATIONS
    # =====================================================

    (
        "ai_regulations",

        "AI Regulations are laws, policies, and guidelines created to ensure AI systems are developed and used safely, fairly, and responsibly.",

        "Governments may regulate high-risk AI systems used in healthcare, finance, or law enforcement.",

        "AI regulations help protect privacy, reduce harmful AI behavior, and improve accountability.",

        "Important AI regulations include GDPR, the EU AI Act, and various national AI governance policies.",

        "How can societies balance AI innovation with safety and ethical responsibility?"
    ),

    (
        "gdpr",

        "GDPR, or the General Data Protection Regulation, is a European law designed to protect personal data and user privacy.",

        "Websites and apps often ask users for permission before collecting personal information because of GDPR requirements.",

        "GDPR gives people more control over how companies collect, store, and use their data.",

        "AI systems that process personal information must comply with privacy regulations like GDPR.",

        "Why should users have control over their personal digital information?"
    ),

    (
        "eu_ai_act",

        "The EU AI Act is a proposed European law that regulates AI systems based on the level of risk they create.",

        "High-risk AI systems used in healthcare or law enforcement may face stricter legal requirements.",

        "The EU AI Act aims to encourage safe, transparent, and responsible AI development.",

        "The law connects AI innovation with accountability and public safety.",

        "Should governments classify AI systems according to their potential risks?"
    ),

    (
        "ai_governance",

        "AI Governance refers to the rules, policies, and frameworks used to guide responsible AI development and use.",

        "Companies may create ethics committees to review how AI systems are designed and deployed.",

        "Good governance helps reduce harmful AI outcomes and improves accountability.",

        "AI Governance combines ethics, regulation, transparency, and oversight.",

        "Why is governance especially important for powerful AI technologies?"
    ),

    (
        "compliance",

        "Compliance means following legal, ethical, and organizational rules related to AI systems.",

        "Organizations using AI must comply with privacy, safety, and fairness regulations.",

        "Compliance helps reduce legal risks, financial penalties, and harmful AI behavior.",

        "AI auditing and governance systems help organizations maintain compliance.",

        "What could happen if companies ignore AI regulations and safety standards?"
    ),

    (
        "ai_auditing",

        "AI Auditing involves reviewing AI systems to evaluate fairness, safety, transparency, and compliance.",

        "Auditors may test whether an AI system unfairly discriminates against certain groups.",

        "AI audits improve accountability and increase public trust in automated systems.",

        "Auditing is an important part of responsible AI governance.",

        "Should independent organizations regularly audit high-risk AI systems?"
    ),

    (
        "ai_standards",

        "AI Standards are guidelines and best practices that help ensure AI systems remain safe, reliable, and consistent.",

        "Organizations may follow international AI safety standards when developing AI technologies.",

        "Standards improve reliability, interoperability, and trust across AI systems.",

        "Global standards support international cooperation in AI governance.",

        "Why are international standards important for rapidly growing AI technologies?"
    ),

    (
        "ai_accountability_laws",

        "AI Accountability Laws are legal rules that hold organizations responsible for the actions and impacts of AI systems.",

        "Companies may face legal consequences if AI systems cause harm or discrimination.",

        "Accountability laws encourage organizations to develop safer and fairer AI systems.",

        "These laws are closely connected to AI governance and auditing practices.",

        "Who should be legally responsible when AI systems make harmful decisions?"
    ),

    (
        "privacy_regulations",

        "Privacy Regulations are laws designed to protect personal information collected and used by organizations and AI systems.",

        "Apps and online platforms must often explain how user data will be collected and stored.",

        "Privacy regulations help reduce surveillance risks and misuse of personal data.",

        "Laws such as GDPR focus heavily on privacy protection and informed consent.",

        "Why do strong privacy protections matter in the age of AI and big data?"
    ),

    (
        "government_ai_policies",

        "Government AI Policies are official strategies and regulations created to guide AI development and use within a country.",

        "Some governments create national AI strategies for education, healthcare, and economic growth.",

        "Government policies help balance AI innovation with ethics, safety, and public protection.",

        "Policies may include rules about transparency, fairness, and responsible AI development.",

        "How should governments balance AI innovation with regulation?"
    ),

    (
        "international_ai_laws",

        "International AI Laws refer to global efforts to create shared rules and agreements for AI technologies.",

        "Countries may cooperate to regulate high-risk AI systems and cybersecurity threats.",

        "International laws can help prevent harmful AI misuse across borders.",

        "Global cooperation becomes increasingly important as AI technologies spread worldwide.",

        "Should countries work together to regulate advanced AI systems globally?"
    ),

    (
        "ethical_regulations",

        "Ethical Regulations are rules designed to ensure AI systems follow moral and social principles.",

        "Organizations may be required to test AI systems for fairness and discrimination before deployment.",

        "Ethical regulations help reduce harm and improve public trust in AI systems.",

        "These regulations are closely connected to responsible AI development.",

        "Should ethical testing become mandatory before releasing powerful AI systems?"
    ),

    (
        "responsible_ai_policies",

        "Responsible AI Policies are organizational guidelines that promote fair, safe, and ethical AI practices.",

        "Technology companies may create internal policies for AI transparency and fairness.",

        "Responsible AI policies help organizations reduce risks and improve accountability.",

        "These policies support trustworthy and human-centered AI development.",

        "Should all companies publicly share their responsible AI policies?"
    ),

    (
        "future_ai_regulations",

        "Future AI Regulations refer to upcoming laws and policies designed to manage increasingly advanced AI technologies.",

        "Governments may introduce stricter rules for autonomous systems and Generative AI tools.",

        "Future regulations will play a major role in balancing innovation, safety, and ethical concerns.",

        "As AI becomes more powerful, global cooperation on regulation may become essential.",

        "How can societies regulate AI without slowing innovation too much?"
    ),


    # =====================================================
    # AI RISKS
    # =====================================================

    (
        "ai_risk",

        "AI Risks refer to the potential dangers, unintended consequences, and harmful effects that AI systems may create for individuals and society.",

        "AI systems can spread misinformation, invade privacy, automate cyberattacks, or make unsafe decisions without proper oversight.",

        "Understanding AI risks helps societies develop safer, more responsible, and better-regulated AI technologies.",

        "AI risks are closely connected to ethics, safety, governance, and human oversight.",

        "How can societies benefit from AI while still reducing its risks?"
    ),

    (
        "misinformation",

        "AI-generated Misinformation refers to false or misleading content created or amplified using AI systems.",

        "AI tools can generate fake news articles, manipulated videos, or misleading social media posts.",

        "Misinformation can influence public opinion, damage trust, and spread confusion quickly online.",

        "Deepfakes and Generative AI technologies are closely linked to misinformation risks.",

        "How can societies detect and reduce AI-generated misinformation?"
    ),

    (
        "deepfakes",

        "Deepfakes are AI-generated videos, images, or audio recordings designed to appear realistic but fake.",

        "AI can create fake celebrity videos or imitate human voices convincingly.",

        "Deepfakes can spread misinformation, damage reputations, and reduce trust in digital media.",

        "Generative AI technologies have made deepfake creation easier and more realistic.",

        "How can people verify whether digital content is real or AI-generated?"
    ),

    (
        "privacy_risks",

        "Privacy Risks in AI involve the misuse, exposure, or excessive collection of personal information.",

        "AI systems may collect user behavior, location, or biometric data without users fully understanding it.",

        "Privacy risks can lead to surveillance, identity theft, and misuse of sensitive information.",

        "Privacy regulations such as GDPR aim to protect user data and digital rights.",

        "Why should users have more control over how their personal data is used?"
    ),

    (
        "surveillance_risks",

        "Surveillance Risks occur when AI systems are used to monitor individuals or populations excessively.",

        "Facial recognition cameras can track people's movements in public spaces.",

        "Excessive surveillance may reduce privacy, freedom, and public trust.",

        "AI surveillance systems raise major ethical and legal concerns worldwide.",

        "How can societies balance public safety with personal privacy?"
    ),

    (
        "cybersecurity_risks",

        "Cybersecurity Risks involve AI systems being used to launch, automate, or strengthen cyberattacks.",

        "Hackers may use AI to automate phishing attacks or discover software vulnerabilities faster.",

        "AI-powered cyber threats can become more advanced, scalable, and difficult to detect.",

        "AI is also used defensively to improve cybersecurity monitoring and threat detection.",

        "Can AI-powered defenses keep up with AI-powered cyberattacks?"
    ),

    (
        "autonomous_weapons",

        "Autonomous Weapons are AI-powered military systems capable of selecting or attacking targets with limited human control.",

        "Some military drones already use AI to assist with navigation and target identification.",

        "Autonomous weapons raise serious concerns about accountability, ethics, and human control in warfare.",

        "Many experts believe international regulations are needed for AI-powered weapons.",

        "Should AI systems ever be allowed to make deadly decisions independently?"
    ),

    (
        "ai_manipulation",

        "AI Manipulation refers to the use of AI systems to influence opinions, behavior, emotions, or decisions unfairly.",

        "Recommendation algorithms may manipulate user attention by promoting emotionally charged content.",

        "Manipulative AI systems can influence politics, consumer behavior, and social interactions.",

        "Social media algorithms and targeted advertising are common examples of AI-driven influence.",

        "How can people protect themselves from AI-driven manipulation?"
    ),

    (
        "hallucinations_ai",

        "AI Hallucinations occur when AI systems generate false, inaccurate, or fabricated information confidently.",

        "Chatbots may sometimes invent facts, fake citations, or incorrect answers that appear believable.",

        "Hallucinations reduce trust in AI systems and can spread misinformation.",

        "AI hallucinations are especially dangerous in healthcare, law, and education.",

        "Why should humans verify important information generated by AI systems?"
    ),

    (
        "overdependence_ai",

        "Overdependence on AI happens when people rely too heavily on AI systems for thinking, decisions, or daily tasks.",

        "Students may depend entirely on AI tools instead of developing problem-solving and critical thinking skills.",

        "Excessive dependence on AI can weaken human judgment, creativity, and independence.",

        "Human oversight remains important even as AI systems become more advanced.",

        "How can people use AI responsibly without becoming overly dependent on it?"
    ),

    (
        "job_displacement_risk",

        "Job Displacement Risk refers to the possibility of workers losing jobs because of AI automation and technological change.",

        "AI chatbots and automation systems can replace repetitive customer support or data-entry tasks.",

        "Understanding workforce risks helps governments and organizations prepare workers for future changes.",

        "AI may also create new industries and careers while replacing older roles.",

        "Which jobs do you think are most likely to change because of AI?"
    ),

    (
        "social_risks",

        "Social Risks of AI refer to the harmful ways AI systems may affect communities, communication, and society.",

        "AI recommendation systems can increase polarization by repeatedly showing users similar viewpoints and content.",

        "Social risks include misinformation, manipulation, inequality, and reduced public trust.",

        "Responsible AI development helps reduce harmful social impacts.",

        "How can AI influence the way people think and interact online?"
    ),

    (
        "ethical_risks",

        "Ethical Risks in AI involve situations where AI systems create unfair, harmful, or morally questionable outcomes.",

        "Biased hiring AI systems may unfairly reject qualified candidates from certain groups.",

        "Ethical risks highlight the importance of fairness, accountability, transparency, and human oversight.",

        "Responsible AI practices help reduce ethical risks in AI systems.",

        "Should companies be legally responsible for unethical AI behavior?"
    ),

    (
        "ai_safety_risks",

        "AI Safety Risks involve the possibility of AI systems behaving unpredictably, dangerously, or outside human control.",

        "A self-driving car making incorrect decisions during emergencies could create serious safety risks.",

        "AI safety becomes increasingly important as AI systems grow more powerful and autonomous.",

        "Researchers study alignment and control methods to improve long-term AI safety.",

        "How can humans ensure advanced AI systems remain safe and controllable?"
    ),

    (
        "loss_human_control",

        "Loss of Human Control refers to situations where AI systems operate beyond meaningful human supervision or understanding.",

        "Highly autonomous AI systems could make decisions faster than humans can react or intervene.",

        "Maintaining human control is critical for safety, accountability, and ethical responsibility.",

        "Human oversight and AI governance help reduce risks from advanced AI systems.",

        "Should humans always retain final authority over important AI decisions?"
    ),

    (
        "future_risks_agi",

        "Future Risks of AGI refer to concerns surrounding Artificial General Intelligence systems that may become more capable than humans in many tasks.",

        "Researchers worry that highly advanced AI systems could behave unpredictably or pursue goals misaligned with human values.",

        "AGI risks could affect global safety, economics, governance, and long-term human survival.",

        "AI safety research and international cooperation are becoming increasingly important for future AI development.",

        "How should humanity prepare for the possibility of extremely advanced AI systems?"
    ),


    
]


cursor.executemany("""

INSERT OR REPLACE INTO learning_content (

    topic_key,
    definition,
    example,
    importance,
    bridge,
    reflection

)

VALUES (?, ?, ?, ?, ?, ?)

""", learning_content)


# ==========================================
# MICRO QUIZZES
# ==========================================

micro_quizzes = [

    (
        "machine_learning",
        "What helps Machine Learning systems improve?",
        "Learning from data",
        "Screen resolution",
        "Keyboard layout",
        "a",
        "Machine Learning systems improve by learning from data."
    ),


    (
        "what_is_ai",
        "What is the main goal of Artificial Intelligence?",
        "Simulate human intelligence",
        "Increase screen brightness",
        "Replace electricity",
        "a",
        "AI systems are designed to simulate tasks requiring human intelligence."
    ),

    (
        "deep_learning",
        "Deep Learning mainly uses:",
        "Neural Networks",
        "Spreadsheet formulas",
        "Manual calculations",
        "a",
        "Deep Learning relies on layered Neural Networks."
    ),

    (
        "nlp",
        "NLP mainly focuses on:",
        "Human language",
        "Battery optimization",
        "Processor manufacturing",
        "a",
        "Natural Language Processing helps AI understand human language."
    ),

    (
        "computer_vision",
        "Computer Vision mainly works with:",
        "Images and videos",
        "Audio cables",
        "Spreadsheet tables",
        "a",
        "Computer Vision helps machines interpret visual information."
    ),

    (
        "generative_ai",
        "Generative AI is mainly used to:",
        "Create new content",
        "Repair hardware",
        "Format databases",
        "a",
        "Generative AI creates text, images, and other forms of content."
    ),

    (
        "ai_healthcare",
        "AI in Healthcare can assist with:",
        "Disease diagnosis",
        "Painting walls",
        "Replacing electricity",
        "a",
        "AI can help doctors detect diseases and analyze patient data."
    ),

    (
        "automation",
        "Automation mainly helps by:",
        "Reducing repetitive tasks",
        "Increasing internet cables",
        "Changing monitor colors",
        "a",
        "Automation improves efficiency by reducing repetitive work."
    ),

    (
        "fairness",
        "What is the goal of fairness in AI?",
        "Avoid discrimination",
        "Increase hardware speed",
        "Reduce internet usage",
        "a",
        "Fairness helps AI systems avoid discriminatory outcomes."
    ),

    (
        "transparency",
        "Transparency in AI means:",
        "AI decisions can be understood",
        "AI systems stay hidden",
        "AI works without data",
        "a",
        "Transparency allows people to understand AI decisions."
    ),

    (
        "data_bias",
        "Data Bias usually occurs when:",
        "Training data is unbalanced",
        "Screens are too bright",
        "Processors are too slow",
        "a",
        "Biased datasets can create unfair AI systems."
    ),

    (
        "gender_bias",
        "Gender Bias in AI may lead to:",
        "Unfair treatment",
        "Faster processors",
        "Better graphics",
        "a",
        "Gender bias can create unfair outcomes for certain groups."
    ),

    (
        "gdpr",
        "GDPR mainly protects:",
        "Personal data",
        "Keyboard layouts",
        "Wi-Fi signals",
        "a",
        "GDPR is focused on data privacy and user protection."
    ),

    (
        "ai_auditing",
        "AI Auditing is mainly used to:",
        "Check fairness and compliance",
        "Increase battery life",
        "Replace operating systems",
        "a",
        "AI audits evaluate systems for fairness, safety, and regulations."
    ),

    (
        "deepfakes",
        "Deepfakes are mainly associated with:",
        "Fake AI-generated media",
        "Network cooling",
        "Hardware assembly",
        "a",
        "Deepfakes use AI to create convincing fake media."
    ),

    (
        "hallucinations_ai",
        "AI hallucinations occur when AI:",
        "Generates false information",
        "Disconnects from servers",
        "Reduces internet speed",
        "a",
        "Hallucinations happen when AI produces fabricated or incorrect content."
    ),

    (
        "loss_human_control",
        "Why is loss of human control considered risky?",
        "AI may act without effective oversight",
        "AI uses too much electricity",
        "AI reduces monitor brightness",
        "a",
        "Advanced autonomous AI may become difficult for humans to control."
    )
]

cursor.executemany("""

INSERT OR REPLACE INTO micro_quizzes (

    topic_key,
    question,
    option_a,
    option_b,
    option_c,
    correct_answer,
    explanation

)

VALUES (?, ?, ?, ?, ?, ?, ?)

""", micro_quizzes)

# ==========================================
# TOPIC CONNECTIONS
# ==========================================

connections = [

    # =====================================================
    # AI BASICS CONNECTIONS
    # =====================================================

    ("what_is_ai", "machine_learning", "foundation"),

    ("machine_learning", "supervised_learning", "subtype"),
    ("machine_learning", "unsupervised_learning", "subtype"),
    ("machine_learning", "reinforcement_learning", "subtype"),
    ("machine_learning", "deep_learning", "advanced_topic"),

    ("deep_learning", "neural_networks", "built_on"),

    ("neural_networks", "computer_vision", "application"),
    ("neural_networks", "nlp", "application"),

    ("nlp", "chatbots", "application"),
    ("nlp", "generative_ai", "advanced_application"),

    ("computer_vision", "ai_transportation", "application"),

    ("training_data", "data_bias", "risk_factor"),

    ("recommendation_systems", "ai_manipulation", "related_risk"),

    ("generative_ai", "deepfakes", "risk_application"),

    ("limitations_ai", "hallucinations_ai", "risk_connection"),

    ("future_of_ai", "ai_governance", "future_concern"),


    # =====================================================
    # AI IMPACT CONNECTIONS
    # =====================================================

    ("ai_healthcare", "ai_privacy", "ethical_concern"),

    ("automation", "job_displacement", "impact"),

    ("economic_impact", "job_displacement", "related_concept"),

    ("social_impact", "misinformation", "societal_risk"),

    ("human_ai_collaboration", "human_oversight", "supporting_concept"),

    ("ai_finance", "algorithmic_bias", "risk_connection"),

    ("ai_education", "responsible_ai", "ethical_need"),


    # =====================================================
    # AI ETHICS CONNECTIONS
    # =====================================================

    ("fairness", "data_bias", "related_concept"),

    ("fairness", "algorithmic_bias", "related_concept"),

    ("transparency", "explainable_ai", "supporting_concept"),

    ("responsible_ai", "trustworthy_ai", "goal"),

    ("trustworthy_ai", "ai_safety", "requirement"),

    ("human_oversight", "loss_human_control", "preventive_measure"),

    ("accountability", "ai_governance", "governance_need"),

    ("ai_privacy", "gdpr", "regulated_by"),


    # =====================================================
    # AI BIAS CONNECTIONS
    # =====================================================

    ("sampling_bias", "data_bias", "cause"),

    ("gender_bias", "hiring_bias", "example"),

    ("racial_bias", "bias_detection", "testing_requirement"),

    ("bias_detection", "reduce_bias", "solution_path"),

    ("algorithmic_bias", "fairness", "ethical_issue"),

    ("data_bias", "responsible_ai", "risk_to"),


    # =====================================================
    # AI REGULATIONS CONNECTIONS
    # =====================================================

    ("gdpr", "ai_privacy", "regulation"),

    ("eu_ai_act", "ai_governance", "legal_framework"),

    ("compliance", "ai_auditing", "verification"),

    ("ai_standards", "responsible_ai", "guideline"),

    ("ai_governance", "accountability", "requires"),

    ("ai_auditing", "trustworthy_ai", "supports"),


    # =====================================================
    # AI RISKS CONNECTIONS
    # =====================================================

    ("misinformation", "deepfakes", "example"),

    ("surveillance_risks", "privacy_risks", "connected_risk"),

    ("cybersecurity_risks", "ai_manipulation", "threat_relation"),

    ("hallucinations_ai", "trustworthy_ai", "trust_issue"),

    ("loss_human_control", "ai_safety", "safety_concern"),

    ("deepfakes", "social_impact", "societal_risk"),

    ("ai_manipulation", "misinformation", "amplifies")

]


cursor.executemany("""

INSERT OR REPLACE INTO topic_connections (

    source_topic,
    connected_topic,
    relationship_type

)

VALUES (?, ?, ?)

""", connections)


# ==========================================
# SAVE CHANGES
# ==========================================

conn.commit()

conn.close()

print("AI Compass learning data inserted successfully.")

# IMPORTANT