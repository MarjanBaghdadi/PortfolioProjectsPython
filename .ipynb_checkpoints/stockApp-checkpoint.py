{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\marjan\\anaconda3\\lib\\site-packages (1.12.2)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (19.2)\n",
      "Requirement already satisfied: semver in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (2.13.0)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (4.12.0)\n",
      "Requirement already satisfied: validators>=0.2 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (7.0)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (6.2.0)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (5.2.0)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (2.8.0)\n",
      "Requirement already satisfied: toml in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (3.20.1)\n",
      "Requirement already satisfied: blinker>=1.0.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (1.5)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (4.3.0)\n",
      "Requirement already satisfied: tzlocal>=1.1 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (4.2)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (6.0.3)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (3.1.27)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (12.5.1)\n",
      "Requirement already satisfied: numpy in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (1.16.5)\n",
      "Requirement already satisfied: altair>=3.2.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (4.2.0)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0b1)\n",
      "Requirement already satisfied: pympler>=0.9 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: watchdog; platform_system != \"Darwin\" in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (2.1.9)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (0.25.1)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: six in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (1.12.0)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (2.4.2)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (0.6.0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from validators>=0.2->streamlit) (4.4.0)\n",
      "Requirement already satisfied: backports.zoneinfo; python_version < \"3.9\" in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.2.1)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: tzdata; platform_system == \"Windows\" in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from tzlocal>=1.1->streamlit) (2022.2)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19->streamlit) (4.0.9)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.13.0)\n",
      "Requirement already satisfied: commonmark<0.10.0,>=0.9.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from rich>=10.11.0->streamlit) (0.9.1)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.0.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.10.0)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.10.3)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2019.3)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.24.2)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.1.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2019.9.11)\n",
      "Requirement already satisfied: more-itertools in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from zipp>=0.5->importlib-metadata>=1.4->streamlit) (7.2.0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (41.4.0)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.15.4)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (19.2.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\marjan\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "%pip install streamlit\n",
    "import streamlit as st\n",
    "\n",
    "st.write(\"\"\"\n",
    "# Simple Stock Price App\n",
    "Shown are the stock closing price and volume of Google!\n",
    "\"\"\")\n",
    "\n",
    "# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75\n",
    "#define the ticker symbol\n",
    "tickerSymbol = 'GOOGL'\n",
    "#get data on this ticker\n",
    "tickerData = yf.Ticker(tickerSymbol)\n",
    "#get the historical prices for this ticker\n",
    "tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')\n",
    "# Open\tHigh\tLow\tClose\tVolume\tDividends\tStock Splits\n",
    "\n",
    "st.line_chart(tickerDf.Close)\n",
    "st.line_chart(tickerDf.Volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
