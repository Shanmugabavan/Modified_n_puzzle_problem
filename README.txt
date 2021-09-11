Settingup Environment
    pip install -r requirements.txt


Play with sample data and Ouput
    1.python main.py
        -output is number of steps will be print by default
        -when passing cmd arguments can generate multiple outputs...... Can easily understand by comment in the code
        -if you want to print path
            python main.py --path

Analysing data with 100 random data
    1.python generator.py generator.py  #code
    2.change file root to 'inputs' and change the seed value to 'i+100'
    3.python generator.py generator.py  #code
    4.Now 100 inputs data in inputs files and goals data in goals files
    5.python random_data_solver.py    # producing manhattan distance
    6.copy that manhattance distance and paste in to 'analyse_manhattan.txt'
    7.python random_data_solver.py --heuristic misplaced  #code
    8.copy that misplaced distance and paste in to 'analyse_misplaced.txt'
    9.python analyser.py
    10.analysing report will be in 'analysis report.txt'    #t- values are only print purpose

