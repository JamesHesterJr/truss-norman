import sys
from Norman import Norman

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    
    for arg in args:
        print('passed argument :: {}'.format(arg))

    inputFilepath = args[0]
    outputFilepath = args[1]

    rules = {
    	'Timestamp': 'TimestampFormat|TimestampTimezoneConversion',
    	'Address': '',
    	'ZIP': 'ZipFormat',
    	'FullName': 'Uppercase',
    	'FooDuration': 'FloatingPointSecond',
    	'BarDuration': 'FloatingPointSecond',
    	'TotalDuration': '',
    	'Notes': ''
    }

    # initialize Norman
    norman = Norman(rules)
    
    # Normalize file
    normalized = norman.normalize(inputFilepath)

if __name__ == '__main__':
    main()