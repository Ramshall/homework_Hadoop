# homework_Hadoop (MapReduce Word Count for UUD 1945)

This project demonstrates how to implement a word count MapReduce program using Hadoop's streaming API. The task involves processing the text of the preamble of the Indonesian Constitution (UUD 1945) and counting the frequency of each word.

## Project Details

The project involves the following steps:
1. **Text Extraction**: Extract the text of the preamble of UUD 1945 from the official website.
2. **Mapper and Reducer Scripts**: Implement a mapper and reducer in Python to count the occurrences of each word.
3. **Hadoop Execution**: Run the mapper and reducer scripts on a Hadoop standalone cluster using `hadoop-streaming-3.2.3.jar`.
4. **Output Handling**: Save the output of the word count to a text file.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ramshall/homework_Hadoop.git
   ```
2. **Run the Jupyter Notebook**:
Open the Homework_Hadoop.ipynb notebook and execute the cells to see the steps in action.

3. **Execute MapReduce on Hadoop**:
Follow the steps outlined in the notebook to run the MapReduce job on Hadoop. You'll need to have Hadoop properly set up on your system.

4. **View the Results**:
The output word count will be saved as pembukaanUUD1945-wordcount.txt.

## Project Structure
* Text Extraction: The first section of the notebook extracts the text from the UUD 1945 website and saves it as pembukaan_uud1945.txt.
* Mapper and Reducer: The Python code for the mapper and reducer scripts is included in the notebook.
* Hadoop Execution: Commands to run the MapReduce job using Hadoop are provided.

## Output Example
The output will be a text file containing the word count of each unique word in the UUD 1945 preamble.

![image](https://github.com/user-attachments/assets/0cd53cb5-b840-4662-928d-ef6f23b5d3ee)
