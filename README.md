# past-paper-compiler
Compile past papers and generate clean sheets based on topics for A-Levels students for targeted revision. 

Problem Statement: Solving past papers is a common way to prepare for upcoming exams. Sometimes students need to practice specific topics using past papers but finding relevant questions one-by-one is time consuming. This project is specifically tailored for this reason which will help students revise better.

Features: You can compile and generate worksheets based on multiple criteria such as topic, year, variant, total marks, etc.

## System Architecture
The Past Paper Compiler operates via a two-stage pipeline: an offline data ingestion engine and a real-time compilation engine.

### 1. Ingestion Pipeline (Data Indexing)
1. **Fetch**: Scrapes raw past paper PDFs directly from online web servers.
2. **Parse**: Reads and parses PDF pages to extract raw question segments.
3. **Classify**: Passes extracted question data to an AI API to analyze and tag each question with its topic, year, variant, component, and mark allocation.
4. **Index**: Stores the categorized metadata and question URLs directly into the relational database.

### 2. Runtime Engine (Worksheet Generation)
5. **Compile**: Queries the database based on user-selected criteria and stitches the matching question clips into a customized PDF worksheet.
