# Week 5 - Technical Assignment Fine tuning using LoRA and PEFT

### Error fixes:
#### Prompt
Formatted prompt needed some enhancing. Old prompt 
```python
f"Instruct: Summarize the following conversation.\n{prompt}\nOutput:\n"
```
was not able to produce any proper summaries of the conversations. The model only started to repeat the conversation when using the word "output". Changing the word "output" to "summary" immediatly changed the model to produce summary of the conversation. The test results improved by 1-2% for the latter test "Absolute percentage improvement of PEFT MODEL over ORIGINAL MODEL".


#### Tensors on different devices
Tensor device dislocation error was fixed by changing the device_map from {"": 0} to "auto".


#### Library version print
Rouge_score library does not have attribute __version__. Thus, the print needed to be commented/removed.
```python
print("Rouge Score version:", rouge_score.__version__)
```


### Screenshot of Hugging Face model
 accessable at https://huggingface.co/raati/TinyLlama-1.1B-dialogsum-finetuned

![image](https://github.com/user-attachments/assets/17571069-a5d4-456d-acb4-a7d7802a803e)



#### Sample outputs

| Summary Type                 | Content |
|------------------------------|---------|
| **Human Baseline Summaries** | Ms. Dawson helps #Person1# to write a memo to inform every employee that they have to change the communication method and should not use Instant Messaging anymore. |
| **Original Model Summaries** | The conversation between a supervisor and an employee discusses the implementation of a new policy regarding the use of Instant Messaging in the workplace. The policy restricts the use of Instant Messaging for all employees, including those who persist in using it. The policy also includes a warning and probationary period for employees who persist in using Instant Messaging. The policy is aimed at reducing time spent on non-work-related communication and ensuring that all communication is conducted through |
| **PEFT Model Summaries** | #Person1# instructs Ms. Dawson to take a dictation for #Person1#'s intra-office memorandum. #Person1#'s new policy restricts all office communications to email correspondence and official memos. |

