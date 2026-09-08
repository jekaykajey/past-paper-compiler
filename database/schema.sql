CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    subject_id INT NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    topic_id INT NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    year INT NOT NULL,
    session VARCHAR(1) NOT NULL,
    paper_number INT NOT NULL,
    variant INT NOT NULL,
    question_number INT NOT NULL,
    mark INT NOT NULL,
    question_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fast lookup for questions by topic, paper number, and year
CREATE INDEX idx_questions_lookup ON questions (topic_id, paper_number, year);

-- Fast lookup for topics by subject
CREATE INDEX idx_topics_subject ON topics (subject_id);