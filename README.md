# past-paper-compiler
Compile past papers and generate clean sheets based on topics for A-Levels students for targeted revision. 

Problem Statement: Solving past papers is a common way to prepare for upcoming exams. Sometimes students need to practice specific topics using past papers but finding relevant questions one-by-one is time consuming. This project is specifically tailored for this reason which will help students revise better.

Features: You can compile and generate worksheets based on multiple criteria such as topic, year, variant, total marks, etc.

System Architecture:
The Past Paper Compiler uses an AI-assisted indexing pipeline and real-time query engine:
1. AI Ingestion & Tagging: Past paper clips from hosted sources are processed via an AI classification API to automatically extract topic tags, mark allocations, and confidence scores.
2. Metadata Indexing: Extracted metadata and file URLs are structured and saved into a database (PostgreSQL/SQLite).
3. Real-time Filtering: Student criteria selections (topic, year range, marks) trigger SQL queries against the indexed metadata.
4. On-demand Compilation: A PDF generator engine fetches matching question clips and stitches them into a custom, printable revision worksheet alongside its mark scheme.
