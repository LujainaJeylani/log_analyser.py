# Log analyser 

A log is a record of events in a computer. My log analyser allows for a log to be searched through, and both a graph and text record to be made about the IP addresses that have been logged and the amount of times they have been logged. This is practical as cybersecurity personnel may be able to use this in order to visualise IP addresses with a low frequency of events in a computer and go back to check on these addresses.

## Limitations

The limitations to this script include: Can only be used for logs containing IP addresses, can only tell least frequently logged IP addresses, no automated actions, limited analyses, no error handling. 
## Usage
To use this script I recommend importing the python file to your preferred code editor(e.g. VS code). Once the python file is imported to the folder of choice, also import your log file, or use the provided log as an example. Once imported, replace the file path on line 48 to the name of your actual file. Once done head to the editor's terminal and use 
```python
python {your_script.py}

```
making sure to replace {your_script.py} with your python script, in my case Log_Analyser.py . Once done the terminal should output a list of top 10 most and least frequented IP addresses within the log -
<img width="708" height="687" alt="image" src="https://github.com/user-attachments/assets/2d2ba920-3425-4fc7-9b3a-278a56f52c94" />


as well as a frequency graph in another window visualising the log -
<img width="1776" height="898" alt="image" src="https://github.com/user-attachments/assets/13593ad4-65c8-4ad8-bee3-fdf77ac6f430" />


## Errors and use cases

If any serious errors leading to harm or inappropriate use of the file I should be contacted immediately, this analyser should not be used in workplace environments dependant on real world problem answers.
