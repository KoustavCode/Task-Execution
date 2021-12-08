The file `config.csv` contains the task log.
Where I have taken another column `Days` for the enhanced version of the task, i.e. handling the day range also.

To execute the code directly on the config execute:

```python
python3 code.py
```
While running it will ask for current time for simple version and days range also for the enhanced version.

Ex: As executed directly on the three enties of the config file.
```python
Current time in HH:MM:SS format : 14:00:00
True
Current time in HH:MM:SS format : 19:00:00
False
Current time in HH:MM:SS format : 18:00:00
Current Day : Wednesday
```
Though, taking the time automatically is added and commented.

To test using nose:
```python
pyhton3 -m node test.py
```
