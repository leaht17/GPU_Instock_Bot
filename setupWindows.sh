#! /bin/bash

py -m venv .env && source .\.env\Scripts\activate && pip install -r requirements.txt && cd GPU_Instock_Bot_V2_src && chmod u+x setupdb.sh && ./setupdb.sh && cd ..
