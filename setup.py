from config import API_KEY, API_SECRET, POLYGON_API_KEY, MONGO_DB_USER, MONGO_DB_PASS, mongo_url
from helper_files.client_helper import strategies
from pymongo import MongoClient
from datetime import datetime
import math
import yfinance as yf
from helper_files.client_helper import get_latest_price
from alpaca.trading.client import TradingClient
from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.timeframe import TimeFrame
from dateutil.relativedelta import relativedelta

def get_timeframes():
   timeframes = {
    "BBANDS_indicator": TimeFrame.Day,
    "DEMA_indicator": TimeFrame.Day,
    "EMA_indicator": TimeFrame.Day,
    "HT_TRENDLINE_indicator": TimeFrame.Day,
    "KAMA_indicator": TimeFrame.Day,
    "MA_indicator": TimeFrame.Day,
    "MAMA_indicator": TimeFrame.Day,
    "MAVP_indicator": TimeFrame.Day,
    "MIDPOINT_indicator": TimeFrame.Day,
    "MIDPRICE_indicator": TimeFrame.Day,
    "SAR_indicator": TimeFrame.Day,
    "SAREXT_indicator": TimeFrame.Day,
    "SMA_indicator": TimeFrame.Day,
    "T3_indicator": TimeFrame.Day,
    "TEMA_indicator": TimeFrame.Day,
    "TRIMA_indicator": TimeFrame.Day,
    "WMA_indicator": TimeFrame.Day,
    "ADX_indicator": TimeFrame.Day,
    "ADXR_indicator": TimeFrame.Day,
    "APO_indicator": TimeFrame.Day,
    "AROON_indicator": TimeFrame.Day,
    "AROONOSC_indicator": TimeFrame.Day,
    "BOP_indicator": TimeFrame.Day,
    "CCI_indicator": TimeFrame.Day,
    "CMO_indicator": TimeFrame.Day,
    "DX_indicator": TimeFrame.Day,
    "MACD_indicator": TimeFrame.Day,
    "MACDEXT_indicator": TimeFrame.Day,
    "MACDFIX_indicator": TimeFrame.Day,
    "MFI_indicator": TimeFrame.Day,
    "MINUS_DI_indicator": TimeFrame.Day,
    "MINUS_DM_indicator": TimeFrame.Day,
    "MOM_indicator": TimeFrame.Day,
    "PLUS_DI_indicator": TimeFrame.Day,
    "PLUS_DM_indicator": TimeFrame.Day,
    "PPO_indicator": TimeFrame.Day,
    "ROC_indicator": TimeFrame.Day,
    "ROCP_indicator": TimeFrame.Day,
    "ROCR_indicator": TimeFrame.Day,
    "ROCR100_indicator": TimeFrame.Day,
    "RSI_indicator": TimeFrame.Day,
    "STOCH_indicator": TimeFrame.Day,
    "STOCHF_indicator": TimeFrame.Day,
    "STOCHRSI_indicator": TimeFrame.Day,
    "TRIX_indicator": TimeFrame.Day,
    "ULTOSC_indicator": TimeFrame.Day,
    "WILLR_indicator": TimeFrame.Day,
    "AD_indicator": TimeFrame.Day,
    "ADOSC_indicator": TimeFrame.Day,
    "OBV_indicator": TimeFrame.Day,
    "HT_DCPERIOD_indicator": TimeFrame.Day,
    "HT_DCPHASE_indicator": TimeFrame.Day,
    "HT_PHASOR_indicator": TimeFrame.Day,
    "HT_SINE_indicator": TimeFrame.Day,
    "HT_TRENDMODE_indicator": TimeFrame.Day,
    "AVGPRICE_indicator": TimeFrame.Day,
    "MEDPRICE_indicator": TimeFrame.Day,
    "TYPPRICE_indicator": TimeFrame.Day,
    "WCLPRICE_indicator": TimeFrame.Day,
    "ATR_indicator": TimeFrame.Day,
    "NATR_indicator": TimeFrame.Day,
    "TRANGE_indicator": TimeFrame.Day,
    "CDL2CROWS_indicator": TimeFrame.Day,
    "CDL3BLACKCROWS_indicator": TimeFrame.Day,
    "CDL3INSIDE_indicator": TimeFrame.Day,
    "CDL3LINESTRIKE_indicator": TimeFrame.Day,
    "CDL3OUTSIDE_indicator": TimeFrame.Day,
    "CDL3STARSINSOUTH_indicator": TimeFrame.Day,
    "CDL3WHITESOLDIERS_indicator": TimeFrame.Day,
    "CDLABANDONEDBABY_indicator": TimeFrame.Day,
    "CDLADVANCEBLOCK_indicator": TimeFrame.Day,
    "CDLBELTHOLD_indicator": TimeFrame.Day,
    "CDLBREAKAWAY_indicator": TimeFrame.Day,
    "CDLCLOSINGMARUBOZU_indicator": TimeFrame.Day,
    "CDLCONCEALBABYSWALL_indicator": TimeFrame.Day,
    "CDLCOUNTERATTACK_indicator": TimeFrame.Day,
    "CDLDARKCLOUDCOVER_indicator": TimeFrame.Day,
    "CDLDOJI_indicator": TimeFrame.Day,
    "CDLDOJISTAR_indicator": TimeFrame.Day,
    "CDLDRAGONFLYDOJI_indicator": TimeFrame.Day,
    "CDLENGULFING_indicator": TimeFrame.Day,
    "CDLEVENINGDOJISTAR_indicator": TimeFrame.Day,
    "CDLEVENINGSTAR_indicator": TimeFrame.Day,
    "CDLGAPSIDESIDEWHITE_indicator": TimeFrame.Day,
    "CDLGRAVESTONEDOJI_indicator": TimeFrame.Day,
    "CDLHAMMER_indicator": TimeFrame.Day,
    "CDLHANGINGMAN_indicator": TimeFrame.Day,
    "CDLHARAMI_indicator": TimeFrame.Day,
    "CDLHARAMICROSS_indicator": TimeFrame.Day,
    "CDLHIGHWAVE_indicator": TimeFrame.Day,
    "CDLHIKKAKE_indicator": TimeFrame.Day,
    "CDLHIKKAKEMOD_indicator": TimeFrame.Day,
    "CDLHOMINGPIGEON_indicator": TimeFrame.Day,
    "CDLIDENTICAL3CROWS_indicator": TimeFrame.Day,
    "CDLINNECK_indicator": TimeFrame.Day,
    "CDLINVERTEDHAMMER_indicator": TimeFrame.Day,
    "CDLKICKING_indicator": TimeFrame.Day,
    "CDLKICKINGBYLENGTH_indicator": TimeFrame.Day,
    "CDLLADDERBOTTOM_indicator": TimeFrame.Day,
    "CDLLONGLEGGEDDOJI_indicator": TimeFrame.Day,
    "CDLLONGLINE_indicator": TimeFrame.Day,
    "CDLMARUBOZU_indicator": TimeFrame.Day,
    "CDLMATCHINGLOW_indicator": TimeFrame.Day,
    "CDLMATHOLD_indicator": TimeFrame.Day,
    "CDLMORNINGDOJISTAR_indicator": TimeFrame.Day,
    "CDLMORNINGSTAR_indicator": TimeFrame.Day,
    "CDLONNECK_indicator": TimeFrame.Day,
    "CDLPIERCING_indicator": TimeFrame.Day,
    "CDLRICKSHAWMAN_indicator": TimeFrame.Day,
    "CDLRISEFALL3METHODS_indicator": TimeFrame.Day,
    "CDLSEPARATINGLINES_indicator": TimeFrame.Day,
    "CDLSHOOTINGSTAR_indicator": TimeFrame.Day,
    "CDLSHORTLINE_indicator": TimeFrame.Day,
    "CDLSPINNINGTOP_indicator": TimeFrame.Day,
    "CDLSTALLEDPATTERN_indicator": TimeFrame.Day,
    "CDLSTICKSANDWICH_indicator": TimeFrame.Day,
    "CDLTAKURI_indicator": TimeFrame.Day,
    "CDLTASUKIGAP_indicator": TimeFrame.Day,
    "CDLTHRUSTING_indicator": TimeFrame.Day,
    "CDLTRISTAR_indicator": TimeFrame.Day,
    "CDLUNIQUE3RIVER_indicator": TimeFrame.Day,
    "CDLUPSIDEGAP2CROWS_indicator": TimeFrame.Day,
    "CDLXSIDEGAP3METHODS_indicator": TimeFrame.Day,
    "BETA_indicator": TimeFrame.Day,
    "CORREL_indicator": TimeFrame.Day,
    "LINEARREG_indicator": TimeFrame.Day,
    "LINEARREG_ANGLE_indicator": TimeFrame.Day,
    "LINEARREG_INTERCEPT_indicator": TimeFrame.Day,
    "LINEARREG_SLOPE_indicator": TimeFrame.Day,
    "STDDEV_indicator": TimeFrame.Day,
    "TSF_indicator": TimeFrame.Day,
    "VAR_indicator": TimeFrame.Day,
}
   return timeframes


def get_relativedeltas():

   indicator_periods = {
      "BBANDS_indicator": relativedelta(years=1),
      "DEMA_indicator": relativedelta(days=30),
      "EMA_indicator": relativedelta(days=30),
      "HT_TRENDLINE_indicator": relativedelta(days=180),
      "KAMA_indicator": relativedelta(days=30),
      "MA_indicator": relativedelta(days=90),
      "MAMA_indicator": relativedelta(days=180),
      "MAVP_indicator": relativedelta(days=90),
      "MIDPOINT_indicator": relativedelta(days=30),
      "MIDPRICE_indicator": relativedelta(days=30),
      "SAR_indicator": relativedelta(days=180),
      "SAREXT_indicator": relativedelta(days=180),
      "SMA_indicator": relativedelta(days=30),
      "T3_indicator": relativedelta(days=30),
      "TEMA_indicator": relativedelta(days=30),
      "TRIMA_indicator": relativedelta(days=30),
      "WMA_indicator": relativedelta(days=30),
      "ADX_indicator": relativedelta(days=90),
      "ADXR_indicator": relativedelta(days=90),
      "APO_indicator": relativedelta(days=30),
      "AROON_indicator": relativedelta(days=90),
      "AROONOSC_indicator": relativedelta(days=90),
      "BOP_indicator": relativedelta(days=30),
      "CCI_indicator": relativedelta(days=30),
      "CMO_indicator": relativedelta(days=30),
      "DX_indicator": relativedelta(days=30),
      "MACD_indicator": relativedelta(days=90),
      "MACDEXT_indicator": relativedelta(days=90),
      "MACDFIX_indicator": relativedelta(days=90),
      "MFI_indicator": relativedelta(days=30),
      "MINUS_DI_indicator": relativedelta(days=30),
      "MINUS_DM_indicator": relativedelta(days=30),
      "MOM_indicator": relativedelta(days=30),
      "PLUS_DI_indicator": relativedelta(days=30),
      "PLUS_DM_indicator": relativedelta(days=30),
      "PPO_indicator": relativedelta(days=30),
      "ROC_indicator": relativedelta(days=30),
      "ROCP_indicator": relativedelta(days=30),
      "ROCR_indicator": relativedelta(days=30),
      "ROCR100_indicator": relativedelta(days=30),
      "RSI_indicator": relativedelta(days=30),
      "STOCH_indicator": relativedelta(days=30),
      "STOCHF_indicator": relativedelta(days=30),
      "STOCHRSI_indicator": relativedelta(days=30),
      "TRIX_indicator": relativedelta(days=30),
      "ULTOSC_indicator": relativedelta(days=180),
      "WILLR_indicator": relativedelta(days=30),
      "AD_indicator": relativedelta(days=30),
      "ADOSC_indicator": relativedelta(days=30),
      "OBV_indicator": relativedelta(days=30),
      "HT_DCPERIOD_indicator": relativedelta(years=2),
      "HT_DCPHASE_indicator": relativedelta(years=2),
      "HT_PHASOR_indicator": relativedelta(years=2),
      "HT_SINE_indicator": relativedelta(years=2),
      "HT_TRENDMODE_indicator": relativedelta(years=2),
      "AVGPRICE_indicator": relativedelta(days=30),
      "MEDPRICE_indicator": relativedelta(days=30),
      "TYPPRICE_indicator": relativedelta(days=30),
      "WCLPRICE_indicator": relativedelta(days=30),
      "ATR_indicator": relativedelta(days=90),
      "NATR_indicator": relativedelta(days=90),
      "TRANGE_indicator": relativedelta(days=90),
      "CDL2CROWS_indicator": relativedelta(days=30),
      "CDL3BLACKCROWS_indicator": relativedelta(days=30),
      "CDL3INSIDE_indicator": relativedelta(days=30),
      "CDL3LINESTRIKE_indicator": relativedelta(days=30),
      "CDL3OUTSIDE_indicator": relativedelta(days=30),
      "CDL3STARSINSOUTH_indicator": relativedelta(days=30),
      "CDL3WHITESOLDIERS_indicator": relativedelta(days=30),
      "CDLABANDONEDBABY_indicator": relativedelta(days=30),
      "CDLADVANCEBLOCK_indicator": relativedelta(days=30),
      "CDLBELTHOLD_indicator": relativedelta(days=30),
      "CDLBREAKAWAY_indicator": relativedelta(days=30),
      "CDLCLOSINGMARUBOZU_indicator": relativedelta(days=30),
      "CDLCONCEALBABYSWALL_indicator": relativedelta(days=30),
      "CDLCOUNTERATTACK_indicator": relativedelta(days=30),
      "CDLDARKCLOUDCOVER_indicator": relativedelta(days=30),
      "CDLDOJI_indicator": relativedelta(days=30),
      "CDLDOJISTAR_indicator": relativedelta(days=30),
      "CDLDRAGONFLYDOJI_indicator": relativedelta(days=30),
      "CDLENGULFING_indicator": relativedelta(days=30),
      "CDLEVENINGDOJISTAR_indicator": relativedelta(days=30),
      "CDLEVENINGSTAR_indicator": relativedelta(days=30),
      "CDLGAPSIDESIDEWHITE_indicator": relativedelta(days=30),
      "CDLGRAVESTONEDOJI_indicator": relativedelta(days=30),
      "CDLHAMMER_indicator": relativedelta(days=30),
      "CDLHANGINGMAN_indicator": relativedelta(days=30),
      "CDLHARAMI_indicator": relativedelta(days=30),
      "CDLHARAMICROSS_indicator": relativedelta(days=30),
      "CDLHIGHWAVE_indicator": relativedelta(days=30),
      "CDLHIKKAKE_indicator": relativedelta(days=30),
      "CDLHIKKAKEMOD_indicator": relativedelta(days=30),
      "CDLHOMINGPIGEON_indicator": relativedelta(days=30),
      "CDLIDENTICAL3CROWS_indicator": relativedelta(days=30),
      "CDLINNECK_indicator": relativedelta(days=30),
      "CDLINVERTEDHAMMER_indicator": relativedelta(days=30),
      "CDLKICKING_indicator": relativedelta(days=30),
      "CDLKICKINGBYLENGTH_indicator": relativedelta(days=30),
      "CDLLADDERBOTTOM_indicator": relativedelta(days=30),
      "CDLLONGLEGGEDDOJI_indicator": relativedelta(days=30),
      "CDLLONGLINE_indicator": relativedelta(days=30),
      "CDLMARUBOZU_indicator": relativedelta(days=30),
      "CDLMATCHINGLOW_indicator": relativedelta(days=30),
      "CDLMATHOLD_indicator": relativedelta(days=30),
      "CDLMORNINGDOJISTAR_indicator": relativedelta(days=30),
      "CDLMORNINGSTAR_indicator": relativedelta(days=30),
      "CDLONNECK_indicator": relativedelta(days=30),
      "CDLPIERCING_indicator": relativedelta(days=30),
      "CDLRICKSHAWMAN_indicator": relativedelta(days=30),
      "CDLRISEFALL3METHODS_indicator": relativedelta(days=30),
      "CDLSEPARATINGLINES_indicator": relativedelta(days=30),
      "CDLSHOOTINGSTAR_indicator": relativedelta(days=30),
      "CDLSHORTLINE_indicator": relativedelta(days=30),
      "CDLSPINNINGTOP_indicator": relativedelta(days=30),
      "CDLSTALLEDPATTERN_indicator": relativedelta(days=30),
      "CDLSTICKSANDWICH_indicator": relativedelta(days=30),
      "CDLTAKURI_indicator": relativedelta(days=30),
      "CDLTASUKIGAP_indicator": relativedelta(days=30),
      "CDLTHRUSTING_indicator": relativedelta(days=30),
      "CDLTRISTAR_indicator": relativedelta(days=30),
      "CDLUNIQUE3RIVER_indicator": relativedelta(days=30),
      "CDLUPSIDEGAP2CROWS_indicator": relativedelta(days=30),
      "CDLXSIDEGAP3METHODS_indicator": relativedelta(days=30),
      "BETA_indicator": relativedelta(years=1),
      "CORREL_indicator": relativedelta(years=1),
      "LINEARREG_indicator": relativedelta(years=2),
      "LINEARREG_ANGLE_indicator": relativedelta(years=2),
      "LINEARREG_INTERCEPT_indicator": relativedelta(years=2),
      "LINEARREG_SLOPE_indicator": relativedelta(years=2),
      "STDDEV_indicator": relativedelta(days=30),
      "TSF_indicator": relativedelta(years=2),
      "VAR_indicator": relativedelta(years=2),
   }
   return indicator_periods


def initialize_algorithms_stats():
   try:
      client = MongoClient(mongo_url)
      db=client.algorithms
      algo_stats_col=db.algo_stats
      
      initialization_date = datetime.now()
      
      indicator_periods=get_relativedeltas()
      timeframes=get_timeframes()
      
      for strategy in strategies:
            strategy_name = strategy.__name__
            
            if not algo_stats_col.find_one({"strategy": strategy_name}):
               
               algo_stats_col.insert_one({  
                  "strategy": strategy_name,  
                  "holdings": {},  
                  "initialized_date": initialization_date,  
                  "score":1,
                  "total_trades": 0,  
                  "successful_trades": 0,
                  "neutral_trades": 0,
                  "failed_trades": 0,   
                  "last_updated": initialization_date, 
                  "timeframe":TimeFrame.Hour,
                  "lookback_interval":indicator_periods[strategy_name]
               })  
            
               algo_stats_col = db.points_tally  
               algo_stats_col.insert_one({  
                  "strategy": strategy_name,  
                  "total_points": 0,  
                  "initialized_date": initialization_date,  
                  "last_updated": initialization_date  
               })  
                  
            
      client.close()
      print("Successfully initialized rank")
   except Exception as exception:
      print(exception)

def insert_rank_to_coefficient(i):
   try:
      client = MongoClient(mongo_url)  
      db = client.trading_simulator 
      collections  = db.rank_to_coefficient
      """
      clear all collections entry first and then insert from 1 to i
      """
      collections.delete_many({})
      for i in range(1, i + 1):
      
         e = math.e
         rate = ((e**e)/(e**2) - 1)
         coefficient = rate**(2 * i)
         collections.insert_one(
            {"rank": i, 
            "coefficient": coefficient
            }
         )
      client.close()
      print("Successfully inserted rank to coefficient")
   except Exception as exception:
      print(exception)
   
  
def initialize_rank():  
   try:
      client = MongoClient(mongo_url)  
      db = client.trading_simulator  
      collections = db.algorithm_holdings  
         
      initialization_date = datetime.now()  


      for strategy in strategies:
         strategy_name = strategy.__name__


         collections = db.algorithm_holdings 
         
         if not collections.find_one({"strategy": strategy_name}):
            
            collections.insert_one({  
               "strategy": strategy_name,  
               "holdings": {},  
               "amount_cash": 50000,  
               "initialized_date": initialization_date,  
               "total_trades": 0,  
               "successful_trades": 0,
               "neutral_trades": 0,
               "failed_trades": 0,   
               "last_updated": initialization_date, 
               "portfolio_value": 50000 
            })  
         
            collections = db.points_tally  
            collections.insert_one({  
               "strategy": strategy_name,  
               "total_points": 0,  
               "initialized_date": initialization_date,  
               "last_updated": initialization_date  
            })  
               
         
      client.close()
      print("Successfully initialized rank")
   except Exception as exception:
      print(exception)

def initialize_time_delta():
   try:
      client = MongoClient(mongo_url)
      db = client.trading_simulator
      collection = db.time_delta
      collection.insert_one({"time_delta": 0.01})
      client.close()
      print("Successfully initialized time delta")
   except Exception as exception:
      print(exception)

def initialize_market_setup():
   try:
      client = MongoClient(mongo_url)
      db = client.market_data
      collection = db.market_status
      collection.insert_one({"market_status": "closed"})
      client.close()
      print("Successfully initialized market setup")
   except Exception as exception:
      print(exception)

def initialize_portfolio_percentages():
   try:
      client = MongoClient(mongo_url)
      stock_client = StockHistoricalDataClient(API_KEY, API_SECRET)
      trading_client = TradingClient(API_KEY, API_SECRET)
      account = trading_client.get_account()
      db = client.trades
      collection = db.portfolio_values
      portfolio_value = float(account.portfolio_value)
      collection.insert_one({
         "name" : "portfolio_percentage",
         "portfolio_value": (portfolio_value-50000)/50000,
      })
      collection.insert_one({
         "name" : "ndaq_percentage",
         "portfolio_value": (get_latest_price('QQQ',stock_client)-503.17)/503.17,
      })
      collection.insert_one({
         "name" : "spy_percentage",
         "portfolio_value": (get_latest_price('SPY',stock_client)-590.50)/590.50,
      })
      client.close()
      print("Successfully initialized portfolio percentages")
   except Exception as exception:
      print(exception)

def initialize_indicator_setup():
   indicator_periods = {
    "BBANDS_indicator": "1y",
    "DEMA_indicator": "1mo",
    "EMA_indicator": "1mo",
    "HT_TRENDLINE_indicator": "6mo",
    "KAMA_indicator": "1mo",
    "MA_indicator": "3mo",
    "MAMA_indicator": "6mo",
    "MAVP_indicator": "3mo",
    "MIDPOINT_indicator": "1mo",
    "MIDPRICE_indicator": "1mo",
    "SAR_indicator": "6mo",
    "SAREXT_indicator": "6mo",
    "SMA_indicator": "1mo",
    "T3_indicator": "1mo",
    "TEMA_indicator": "1mo",
    "TRIMA_indicator": "1mo",
    "WMA_indicator": "1mo",
    "ADX_indicator": "3mo",
    "ADXR_indicator": "3mo",
    "APO_indicator": "1mo",
    "AROON_indicator": "3mo",
    "AROONOSC_indicator": "3mo",
    "BOP_indicator": "1mo",
    "CCI_indicator": "1mo",
    "CMO_indicator": "1mo",
    "DX_indicator": "1mo",
    "MACD_indicator": "3mo",
    "MACDEXT_indicator": "3mo",
    "MACDFIX_indicator": "3mo",
    "MFI_indicator": "1mo",
    "MINUS_DI_indicator": "1mo",
    "MINUS_DM_indicator": "1mo",
    "MOM_indicator": "1mo",
    "PLUS_DI_indicator": "1mo",
    "PLUS_DM_indicator": "1mo",
    "PPO_indicator": "1mo",
    "ROC_indicator": "1mo",
    "ROCP_indicator": "1mo",
    "ROCR_indicator": "1mo",
    "ROCR100_indicator": "1mo",
    "RSI_indicator": "1mo",
    "STOCH_indicator": "1mo",
    "STOCHF_indicator": "1mo",
    "STOCHRSI_indicator": "1mo",
    "TRIX_indicator": "1mo",
    "ULTOSC_indicator": "6mo",
    "WILLR_indicator": "1mo",
    "AD_indicator": "1mo",
    "ADOSC_indicator": "1mo",
    "OBV_indicator": "1mo",
    "HT_DCPERIOD_indicator": "2y",
    "HT_DCPHASE_indicator": "2y",
    "HT_PHASOR_indicator": "2y",
    "HT_SINE_indicator": "2y",
    "HT_TRENDMODE_indicator": "2y",
    "AVGPRICE_indicator": "1mo",
    "MEDPRICE_indicator": "1mo",
    "TYPPRICE_indicator": "1mo",
    "WCLPRICE_indicator": "1mo",
    "ATR_indicator": "3mo",
    "NATR_indicator": "3mo",
    "TRANGE_indicator": "3mo",
    "CDL2CROWS_indicator": "1mo",
    "CDL3BLACKCROWS_indicator": "1mo",
    "CDL3INSIDE_indicator": "1mo",
    "CDL3LINESTRIKE_indicator": "1mo",
    "CDL3OUTSIDE_indicator": "1mo",
    "CDL3STARSINSOUTH_indicator": "1mo",
    "CDL3WHITESOLDIERS_indicator": "1mo",
    "CDLABANDONEDBABY_indicator": "1mo",
    "CDLADVANCEBLOCK_indicator": "1mo",
    "CDLBELTHOLD_indicator": "1mo",
    "CDLBREAKAWAY_indicator": "1mo",
    "CDLCLOSINGMARUBOZU_indicator": "1mo",
    "CDLCONCEALBABYSWALL_indicator": "1mo",
    "CDLCOUNTERATTACK_indicator": "1mo",
    "CDLDARKCLOUDCOVER_indicator": "1mo",
    "CDLDOJI_indicator": "1mo",
    "CDLDOJISTAR_indicator": "1mo",
    "CDLDRAGONFLYDOJI_indicator": "1mo",
    "CDLENGULFING_indicator": "1mo",
    "CDLEVENINGDOJISTAR_indicator": "1mo",
    "CDLEVENINGSTAR_indicator": "1mo",
    "CDLGAPSIDESIDEWHITE_indicator": "1mo",
    "CDLGRAVESTONEDOJI_indicator": "1mo",
    "CDLHAMMER_indicator": "1mo",
    "CDLHANGINGMAN_indicator": "1mo",
    "CDLHARAMI_indicator": "1mo",
    "CDLHARAMICROSS_indicator": "1mo",
    "CDLHIGHWAVE_indicator": "1mo",
    "CDLHIKKAKE_indicator": "1mo",
    "CDLHIKKAKEMOD_indicator": "1mo",
    "CDLHOMINGPIGEON_indicator": "1mo",
    "CDLIDENTICAL3CROWS_indicator": "1mo",
    "CDLINNECK_indicator": "1mo",
    "CDLINVERTEDHAMMER_indicator": "1mo",
    "CDLKICKING_indicator": "1mo",
    "CDLKICKINGBYLENGTH_indicator": "1mo",
    "CDLLADDERBOTTOM_indicator": "1mo",
    "CDLLONGLEGGEDDOJI_indicator": "1mo",
    "CDLLONGLINE_indicator": "1mo",
    "CDLMARUBOZU_indicator": "1mo",
    "CDLMATCHINGLOW_indicator": "1mo",
    "CDLMATHOLD_indicator": "1mo",
    "CDLMORNINGDOJISTAR_indicator": "1mo",
    "CDLMORNINGSTAR_indicator": "1mo",
    "CDLONNECK_indicator": "1mo",
    "CDLPIERCING_indicator": "1mo",
    "CDLRICKSHAWMAN_indicator": "1mo",
    "CDLRISEFALL3METHODS_indicator": "1mo",
    "CDLSEPARATINGLINES_indicator": "1mo",
    "CDLSHOOTINGSTAR_indicator": "1mo",
    "CDLSHORTLINE_indicator": "1mo",
    "CDLSPINNINGTOP_indicator": "1mo",
    "CDLSTALLEDPATTERN_indicator": "1mo",
    "CDLSTICKSANDWICH_indicator": "1mo",
    "CDLTAKURI_indicator": "1mo",
    "CDLTASUKIGAP_indicator": "1mo",
    "CDLTHRUSTING_indicator": "1mo",
    "CDLTRISTAR_indicator": "1mo",
    "CDLUNIQUE3RIVER_indicator": "1mo",
    "CDLUPSIDEGAP2CROWS_indicator": "1mo",
    "CDLXSIDEGAP3METHODS_indicator": "1mo",
    "BETA_indicator": "1y",
    "CORREL_indicator": "1y",
    "LINEARREG_indicator": "2y",
    "LINEARREG_ANGLE_indicator": "2y",
    "LINEARREG_INTERCEPT_indicator": "2y",
    "LINEARREG_SLOPE_indicator": "2y",
    "STDDEV_indicator": "1mo",
    "TSF_indicator": "2y",
    "VAR_indicator": "2y",
   }
   try:
      client = MongoClient(mongo_url)
      db = client["IndicatorsDatabase"]
      collection = db["Indicators"]

      # Insert indicators into the collection
      for indicator, period in indicator_periods.items():
         collection.insert_one({"indicator": indicator, "ideal_period": period})

      print("Indicators and their ideal periods have been inserted into MongoDB.")
   except Exception as e:
      print(e)
      return

def initialize_historical_database_cache():
   try:
      client = MongoClient(mongo_url)
      db = client["HistoricalDatabase"]
      collection = db["HistoricalDatabase"]
   except:
      print("Error initializing historical database cache")
      return

if __name__ == "__main__":
   
   insert_rank_to_coefficient(200)
   
   initialize_rank()
   
   initialize_time_delta()
   
   initialize_market_setup()
   
   initialize_portfolio_percentages()

   initialize_indicator_setup()
   
   initialize_historical_database_cache()