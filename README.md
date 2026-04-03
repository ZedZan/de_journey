# DE Journey 🚀

## What is this?
A self-directed Data Engineering learning project built over 13 weeks.
Currently at Week 4 — covering ETL pipelines, SQL modeling, OOP, 
Docker, and automation.

## Tech Stack
- **Python 3.11** — ETL pipelines, data transformation
- **PostgreSQL** — data storage and Star Schema modeling
- **Docker & docker-compose** — containerized infrastructure
- **pytest** — automated testing
- **black & flake8** — code quality
- **Makefile** — workflow automation

## Project Structure
de-journey/
├── docker-compose.yml
├── Makefile
├── week1/  → ETL pipeline fundamentals
├── week2/  → Star Schema & SQL analytics
└── week3/  → OOP pipelines & pydantic config

## How to Run
1. Clone the repo
2. Start infrastructure:
   \`\`\`bash
   make up
   \`\`\`
3. Load data:
   \`\`\`bash
   make setup
   \`\`\`
4. Run pipeline:
   \`\`\`bash
   make run
   \`\`\`
5. Run tests:
   \`\`\`bash
   make test
   \`\`\`

## What I learned
- How to build production-grade ETL pipelines in Python
- Star Schema design and analytical SQL queries
- OOP patterns for reusable pipelines
- Docker containerization and docker-compose
- Testing with pytest and mocking
- Code quality with black and flake8
