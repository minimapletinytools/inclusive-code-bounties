# INCLUSIVE ENGLISH LANGUAGE DICTIONARY

The idea is to create a dictionary file of biased English terms to be used in an inclusive language spellchecker. It should have words comparable to those in the inclusiveness feature of Microsoft Office since 2017.

The dictionary can be converted into JSON format as it is easily machine parse-able. Use `parse_data.py` script for this purpose. The output is stored in `bias_data.json` by default. To overide, add `--save_to=<filename>` argument to save to a specific JSON file. Replace `<filename>` with a filename like `output.json`.

# FORMAT

```
<biased word>: <alternative word>, <another alternative word>,...
```
# CATEGORIES

- Cultural Bias
- Disability Bias
- Ethnic Slurs
- Gender Bias
- Sexual Orientation Bias

# CONTRIBUTORS

* [@srisankethu](https://github.com/srisankethu)
