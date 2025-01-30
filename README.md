# project_python




# Coverage 
To check the coverage run this command in the project root \GIT_repositories\project_python>
python -m pytest --cov=src --cov-report=term-missing test/

Generates a report with the coverage located in GIT_repositories\project_python\htmlcov
python -m pytest --cov=src --cov-report=html --html=report.html test/

The file index.html is possible see as green and red the lines covered

# Report
To generate the test report run this command in the project root \GIT_repositories\project_python> 
python -m pytest --html=report.html

# Report and Coverage
To generate the test report and coverage run this command in the project root \GIT_repositories\project_python> 
python -m pytest --cov=src --cov-report=term-missing --html=report.html --self-contained-html test/
