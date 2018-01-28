# Introduction
This repository provides code that converts the zipped XML datasets for
[SemEval 2016][semeval2016] and [2017][semeval2017] English Task 3, Subtask B
into a single dataset in JSON.

 [semeval2016]: http://alt.qcri.org/semeval2016/task3/
 [semeval2017]: http://alt.qcri.org/semeval2017/task3/

# Usage
Use the program as follows:

    $ pip install -r requirements.txt
    $ python __main__.py
     79% [........................................................               ] 17186816 / 21555267

The resulting dataset will reside in the `result.json` file.

# References
You should use the following citation in your publications whenever using this resource:

    @InProceedings{nakov-EtAl:2016:SemEval,
      author    = {Nakov, Preslav  and  M\`{a}rquez, Llu\'{i}s  and  Magdy, Walid  and  Moschitti, Alessandro  and  Glass, Jim  and  Randeree, Bilal},
      title     = {{SemEval}-2016 Task 3: Community Question Answering},
      booktitle = {Proceedings of the 10th International Workshop on Semantic Evaluation},
      series    = {SemEval '16},
      month     = {June},
      year      = {2016},
      address   = {San Diego, California},
      publisher = {Association for Computational Linguistics},
    }

    @InProceedings{SemEval-2017:task3,
       author    = {Nakov, Preslav and Hoogeveen, Doris and M\`{a}rquez, Llu\'{i}s and Moschitti, Alessandro and Mubarak, Hamdy and Baldwin, Timothy and Verspoor, Karin},
       title     = {{SemEval}-2017 Task 3: Community Question Answering},
       booktitle = {Proceedings of the 11th International Workshop on Semantic Evaluation},
       series    = {SemEval '17},
       month     = {August},
       year      = {2017},
       address   = {Vancouver, Canada},
       publisher = {Association for Computational Linguistics},
     }
