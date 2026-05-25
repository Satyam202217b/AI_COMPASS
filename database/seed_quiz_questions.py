import sqlite3

conn = sqlite3.connect("database/ai_compass.db")

cursor = conn.cursor()

questions = [

    (
        "ai_basics",

        "Which type of Machine Learning uses labeled training data to predict outcomes?",

        "Reinforcement Learning",
        "Unsupervised Learning",
        "Supervised Learning",

        "c",

        "Supervised Learning uses labeled training data to make predictions."
    ),

    (
        "ai_basics",

        "Which AI approach focuses on identifying hidden patterns without labeled data?",

        "Supervised Learning",
        "Deep Learning",
        "Unsupervised Learning",

        "c",

        "Unsupervised Learning identifies patterns and relationships in unlabeled data."
    ),

    (
        "ai_basics",

        "Which statement best describes Reinforcement Learning?",

        "Learning through rewards and penalties",
        "Learning only from labeled datasets",
        "Learning without any feedback",

        "a",

        "Reinforcement Learning improves decisions using rewards and penalties."
    ),

    (
        "ai_basics",

        "Neural Networks are inspired by which biological structure?",

        "Human brain neurons",
        "Computer processors",
        "Database tables",

        "a",

        "Neural Networks are modeled after interconnected neurons in the human brain."
    ),

    (
        "ai_basics",

        "Which AI field mainly focuses on understanding human language?",

        "Computer Vision",
        "Natural Language Processing",
        "Cloud Computing",

        "b",

        "NLP enables machines to process and understand human language."
    ),

    (
        "ai_basics",

        "What is the primary purpose of Generative AI?",

        "Store structured data",
        "Generate new content",
        "Optimize processors",

        "b",

        "Generative AI creates text, images, audio, and other forms of content."
    ),

    (
        "ai_basics",

        "Which of the following is an example of Computer Vision?",

        "Image recognition",
        "Database indexing",
        "Packet routing",

        "a",

        "Computer Vision enables machines to interpret and analyze visual information."
    ),

    (
        "ai_basics",

        "Training data is mainly used in AI systems to:",

        "Improve model learning",
        "Delete algorithms",
        "Reduce storage space",

        "a",

        "Training data teaches AI models patterns and relationships."
    ),

    (
        "ai_basics",

        "Recommendation systems mainly work by:",

        "Predicting user preferences",
        "Increasing hardware speed",
        "Compressing files",

        "a",

        "Recommendation systems analyze behavior to predict user interests."
    ),

    (
        "ai_basics",

        "Which is considered a limitation of AI?",

        "Perfect ethical reasoning",
        "Dependence on data quality",
        "Unlimited understanding",

        "b",

        "AI systems depend heavily on the quality and diversity of data."
    ),

    (
        "ai_basics",

        "Deep Learning is a subset of:",

        "Machine Learning",
        "Networking",
        "Cybersecurity",

        "a",

        "Deep Learning is an advanced branch of Machine Learning."
    ),

    (
        "ai_impact",

        "Which healthcare task commonly uses AI?",

        "Disease diagnosis assistance",
        "Hard disk formatting",
        "Keyboard optimization",

        "a",

        "AI helps healthcare professionals analyze diseases and medical images."
    ),

    (
        "ai_impact",

        "AI in education is commonly used for:",

        "Personalized learning",
        "Processor manufacturing",
        "Cable management",

        "a",

        "AI can personalize learning experiences for students."
    ),

    (
        "ai_impact",

        "Fraud detection in finance mainly depends on AI for:",

        "Risk pattern analysis",
        "Screen calibration",
        "Hardware assembly",

        "a",

        "AI analyzes transaction patterns to detect fraud."
    ),

    (
        "ai_impact",

        "Self-driving vehicles are most closely related to AI in:",

        "Transportation",
        "Agriculture",
        "Entertainment",

        "a",

        "AI enables autonomous driving and traffic analysis."
    ),

    (
        "ai_impact",

        "AI in agriculture is often used for:",

        "Crop monitoring",
        "Compiler design",
        "Memory allocation",

        "a",

        "AI assists farmers through crop monitoring and predictive analysis."
    ),

    (
        "ai_impact",

        "Which AI application focuses on detecting cyber threats?",

        "AI in Cybersecurity",
        "AI in Creativity",
        "AI in Agriculture",

        "a",

        "AI in Cybersecurity helps identify attacks and unusual activity."
    ),

    (
        "ai_impact",

        "Automation using AI mainly helps by:",

        "Reducing repetitive tasks",
        "Eliminating all jobs",
        "Removing all human decisions",

        "a",

        "Automation increases efficiency by reducing repetitive manual work."
    ),

    (
        "ai_impact",

        "Human-AI collaboration means:",

        "Humans and AI working together",
        "Humans being fully replaced",
        "AI operating without supervision",

        "a",

        "Human-AI collaboration combines human judgment with AI efficiency."
    ),

    (
        "ai_impact",

        "Which AI impact is most associated with workforce concerns?",

        "Computer Vision",
        "Job Displacement",
        "Data Compression",

        "b",

        "Job displacement is a major concern regarding AI automation."
    ),

    (
        "ai_ethics",

        "Fairness in AI mainly refers to:",

        "Equal treatment across groups",
        "Faster execution speed",
        "Bigger datasets",

        "a",

        "Fairness ensures AI systems do not discriminate unfairly."
    ),

    (
        "ai_ethics",

        "Explainable AI focuses on making AI systems:",

        "Easier to understand",
        "Harder to access",
        "Fully autonomous",

        "a",

        "Explainable AI helps humans understand AI decisions."
    ),

    (
        "ai_ethics",

        "Transparency in AI primarily means:",

        "Visibility into AI decisions",
        "Open internet access",
        "Removing encryption",

        "a",

        "Transparency allows users to understand how AI systems work."
    ),

    (
        "ai_ethics",

        "Responsible AI development includes:",

        "Minimizing harm and bias",
        "Ignoring ethical concerns",
        "Avoiding regulations",

        "a",

        "Responsible AI aims to create safe and ethical systems."
    ),

    (
        "ai_ethics",

        "Which concept ensures humans can intervene in AI decisions?",

        "Human Oversight",
        "Neural Scaling",
        "Tokenization",

        "a",

        "Human oversight ensures humans remain in control of critical AI systems."
    ),

    (
        "ai_ethics",

        "AI Privacy mainly deals with:",

        "Protecting personal data",
        "Increasing bandwidth",
        "Cooling processors",

        "a",

        "AI privacy focuses on protecting user and organizational data."
    ),

    (
        "ai_ethics",

        "Trustworthy AI systems should be:",

        "Reliable and ethical",
        "Random and unpredictable",
        "Completely secretive",

        "a",

        "Trustworthy AI must be dependable, fair, and transparent."
    ),

    (
        "ai_ethics",

        "Ethical decision making in AI is concerned with:",

        "Moral consequences",
        "Storage capacity",
        "Hardware speed",

        "a",

        "Ethical AI evaluates the moral impact of AI decisions."
    ),

    (
        "ai_bias",

        "AI Bias occurs when:",

        "AI produces unfair outcomes",
        "Databases fail",
        "Processors overheat",

        "a",

        "AI bias results in unfair or discriminatory outcomes."
    ),

    (
        "ai_bias",

        "Sampling Bias happens when:",

        "Data is not representative",
        "Models are too small",
        "Internet speed is low",

        "a",

        "Sampling bias occurs when training data does not represent the real population."
    ),

    (
        "ai_bias",

        "Algorithmic Bias is mainly caused by:",

        "Unfair model logic",
        "Storage limitations",
        "Weak internet connections",

        "a",

        "Algorithmic bias occurs because of biased design or model assumptions."
    ),

    (
        "ai_bias",

        "Which is an example of Gender Bias in AI?",

        "Favoring one gender unfairly",
        "Compressing files differently",
        "Improving recommendations equally",

        "a",

        "Gender bias occurs when AI treats genders unfairly."
    ),

    (
        "ai_bias",

        "Facial recognition bias is commonly linked to:",

        "Unequal recognition accuracy",
        "Faster image rendering",
        "Audio processing",

        "a",

        "Facial recognition systems may perform differently across demographic groups."
    ),

    (
        "ai_bias",

        "Fairness testing is mainly used to:",

        "Detect discrimination",
        "Increase processor speed",
        "Delete datasets",

        "a",

        "Fairness testing checks AI systems for discriminatory behavior."
    ),

    (
        "ai_bias",

        "Which method helps reduce AI bias?",

        "Using diverse datasets",
        "Reducing transparency",
        "Ignoring fairness testing",

        "a",

        "Diverse datasets help reduce unfair bias in AI systems."
    ),

    (
        "ai_regulations",

        "GDPR mainly focuses on:",

        "Data privacy and protection",
        "Robot manufacturing",
        "Processor optimization",

        "a",

        "GDPR regulates personal data privacy and protection."
    ),

    (
        "ai_regulations",

        "The EU AI Act mainly aims to:",

        "Regulate AI based on risk",
        "Ban all AI systems",
        "Replace machine learning",

        "a",

        "The EU AI Act classifies AI systems according to risk levels."
    ),

    (
        "ai_regulations",

        "AI Governance primarily refers to:",

        "Managing responsible AI use",
        "Building processors",
        "Increasing internet speed",

        "a",

        "AI Governance establishes rules and practices for AI systems."
    ),

    (
        "ai_regulations",

        "Compliance in AI means:",

        "Following legal requirements",
        "Removing transparency",
        "Reducing storage space",

        "a",

        "Compliance ensures AI systems meet legal and ethical standards."
    ),

    (
        "ai_regulations",

        "AI auditing is mainly conducted to:",

        "Detect issues in AI systems",
        "Upgrade hardware",
        "Increase bandwidth",

        "a",

        "AI audits help evaluate fairness, transparency, and safety."
    ),

    (
        "ai_regulations",

        "Which regulation area mainly protects personal information?",

        "Privacy Regulations",
        "Graphics Standards",
        "Networking Protocols",

        "a",

        "Privacy regulations protect user data and personal information."
    ),

    (
        "ai_risks",

        "Deepfakes are primarily associated with:",

        "AI-generated fake media",
        "Database corruption",
        "Processor simulation",

        "a",

        "Deepfakes use AI to create realistic fake videos or images."
    ),

    (
        "ai_risks",

        "Hallucinations in AI occur when models:",

        "Generate false information",
        "Disconnect from servers",
        "Compress files incorrectly",

        "a",

        "AI hallucinations happen when models produce inaccurate or fabricated responses."
    ),

    (
        "ai_risks",

        "Surveillance risks in AI are mainly connected to:",

        "Excessive monitoring",
        "Better camera quality",
        "Faster rendering",

        "a",

        "AI surveillance risks involve privacy invasion and constant monitoring."
    ),

    (
        "ai_risks",

        "Which AI risk involves influencing people using generated content?",

        "AI Manipulation",
        "Data Compression",
        "System Backup",

        "a",

        "AI manipulation can influence opinions and behavior using generated content."
    ),

    (
        "ai_risks",

        "Overdependence on AI may result in:",

        "Reduced human critical thinking",
        "Better handwriting",
        "Lower electricity usage",

        "a",

        "Excessive dependence on AI may weaken human decision-making skills."
    ),

    (
        "ai_risks",

        "Autonomous weapons are risky because they:",

        "Can operate with limited human control",
        "Improve education systems",
        "Reduce cybersecurity threats",

        "a",

        "Autonomous weapons may make life-critical decisions without sufficient human oversight."
    ),

    (
        "ai_risks",

        "Which concern is most associated with AGI risks?",

        "Loss of human control",
        "Lower storage space",
        "Reduced internet speed",

        "a",

        "Advanced AGI systems could potentially exceed human control."
    ),

    (
        "ai_risks",

        "Misinformation spreads rapidly using AI because:",

        "AI can generate realistic content at scale",
        "AI blocks social media",
        "AI disables communication systems",

        "a",

        "AI enables fast creation of convincing misinformation."
    ),

    (
        "ai_ethics",

        "Which combination best represents ethical AI development?",

        "Transparency, accountability, and fairness",
        "Secrecy, manipulation, and surveillance",
        "Complexity, bias, and misinformation",

        "a",

        "Ethical AI systems should be transparent, accountable, and fair."
    ),

    (
        "ai_basics",

        "Which AI model type is commonly used for image recognition tasks?",

        "Neural Networks",
        "Spreadsheet Models",
        "File Systems",

        "a",

        "Neural Networks are widely used in image recognition applications."
    )

]

cursor.executemany("""

INSERT INTO quiz_questions (

    topic_key,
    question,
    option_a,
    option_b,
    option_c,
    correct_answer,
    explanation

)

VALUES (?, ?, ?, ?, ?, ?, ?)

""", questions)

conn.commit()

conn.close()

print("Quiz questions inserted successfully.")