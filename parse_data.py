import argparse
import json
import requests


if __name__ == "__main__":

	#Add biases
    bias_files = {
                  "cultural_bias": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/cultural_bias.md",
                  "disability_bias": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/disability_bias.md",
                  "ethnic_slurs": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/ethnic_slurs.md",
                  "gender_bias": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/gender_bias.md",
                  "gender_specific_language": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/gender_specific_language.md",
                  "sexual_orientation_bias": "https://raw.githubusercontent.com/srisankethu/inclusive-code-bounties/main/sexual_orientation_bias.md"
                  }

    try:

    	parser = argparse.ArgumentParser()
    	parser.add_argument('--save_to', type=str, dest='output_filename', default="bias_data.json")

    	args = parser.parse_known_args() #Can use this to handle additional new arguments

    	if '.json' not in args[0].output_filename and '.JSON' not in args[0].output_filename:
    		raise Exception("Invalid output filename")
        
        bias_dict = {}
        for bias in bias_files.keys():
    	    r = requests.get(bias_files.get(bias))
    	    data = r.text
    	    lines = data.splitlines()

    	    words_dict = {}
    	    for line in lines:
    		    words = line.split(":")
    			
    		    biased_word = words[0].encode('utf-8')
    		    word_alternatives = [w.strip().encode('utf-8') for w in words[1].split(",")]

    		    words_dict[biased_word] = word_alternatives

    	    bias_dict[bias] = words_dict

        output_file = open(args[0].output_filename, "w")
        json.dump(bias_dict, output_file)
        output_file.close()
    except Exception as e:
    	print(e)
    	