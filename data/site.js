const SITE={
  email:["ashiqurrahmankhan04","gmail.com"],
  web3formsKey:"1fcf6862-b9d6-4bf2-a2f6-8cbc38be31e6"
};
const PROJECTS=[
  {
    slug:"dengue",
    title:"Forecasting dengue hospital admissions in Bangladesh",
    repo:"Bangladesh-Dengue-Forecasting-Analysis",
    image:"assets/projects/dengue.jpg",
    year:"2026",
    field:"Public health, time series forecasting",
    summary:"Weekly forecasts one to four weeks ahead for the eight divisions, built on DGHS dashboard data from 2023 to 2026, with data repair, a weather lag model, five forecasting models and a Power BI dashboard.",
    result:"Only XGBoost was clearly better than repeating last week in both test years.",
    intro:"Weekly forecasts one to four weeks ahead for the eight divisions of Bangladesh, built on DGHS dashboard data from 2023 to 2026, with data repair, seasonality, a weather lag model, five forecasting models and a Power BI dashboard.",
    question:"How many dengue admissions should each division expect in the next one to four weeks, and how far can that forecast be trusted?",
    data:"592,614 hospital admissions and 2,912 deaths over 195 weeks, up to the week of 20 September 2026. DGHS publishes the counts only as charts on a dashboard, so the numbers were read out of the chart code, checked against each other and repaired.",
    tools:["R (forecast, dlnm)","Python","DuckDB SQL","XGBoost","Power BI"],
    findings:[
      {stat:"105,000",title:"The data needed repair before any model could be trusted",text:"About 105,000 admissions were missing from the 2023 division series. Dhaka stopped counting its two city corporations and Barishal reported zero at its own peak. Both were rebuilt from 176 daily DGHS press releases."},
      {stat:"3 times",title:"2023 was about three times the size of the years after it",text:"316,906 admissions in 2023, against 100,971 in 2024 and 102,788 in 2025. By week 39, 2026 was running at 1.58 times 2025 at the same week."},
      {stat:"401 per 100,000",title:"Per person, Barishal is hit hardest, not Dhaka",text:"Barishal had the highest admission rate in three of the four years. Dhaka division's share of national admissions fell from 53.5% in 2023 to 40.3% in 2026 so far."},
      {stat:"61% male",title:"Young men are admitted most, but women and older people die more often",text:"Ages 16 to 30 are 40% of admissions and 61% of admissions are male. Women are 37% to 40% of admissions in each year but 48% to 57% of deaths."},
      {stat:"0.12",title:"Most of the weather signal was the calendar",text:"Admissions correlate at 0.5 to 0.8 with rain, temperature and dew point six to ten weeks earlier. Once the yearly cycle is removed from both, the strongest correlation left is 0.12."},
      {stat:"p = 0.028",title:"Only XGBoost clearly beat repeating last week in both years",text:"No model won both years: XGBoost led in 2025 and ARIMA with Fourier terms in 2026. On Diebold-Mariano tests only XGBoost beat the last-value forecast in both, p = 0.028 and 0.025."}
    ],
    methods:[
      "Read the daily and weekly counts out of the DGHS dashboard's chart code, with one dated snapshot per year.",
      "Audited and repaired the series, rebuilding Dhaka and Barishal for 2023 from 176 daily press releases, with every rule logged.",
      "Answered 11 questions in DuckDB SQL, including the two no-model forecasts every model has to beat.",
      "Set the modelling rules in the EDA on 2023 to 2025 only, so the test year stayed out of every choice.",
      "Trained XGBoost with quantile ranges and a random forest, one model per horizon, retrained every week as rolling forecasts.",
      "Measured seasonality with STL and the weather effect with a distributed lag non-linear model in R.",
      "Fitted ARIMA with Fourier terms by Box-Jenkins, ETS and a negative binomial model, then scored all models on the same 2,912 forecasts.",
      "Built an 8-page Power BI dashboard on 47 tables that only displays the results."
    ],
    shots:[
      {src:"assets/projects/dengue/1.jpg",caption:"Executive summary"},
      {src:"assets/projects/dengue/2.jpg",caption:"Geography"},
      {src:"assets/projects/dengue/3.jpg",caption:"Forecasts"},
      {src:"assets/projects/dengue/4.jpg",caption:"Model comparison"}
    ],
    links:[{label:"Read the full report",path:"Bangladesh%20Dengue%20Forecasting%20Analysis%20Report.pdf"}]
  },
  {
    slug:"nhanes",
    title:"Cardiometabolic risk and mortality in US adults",
    repo:"NHANES-Cardiometabolic-Mortality-Analysis",
    image:"assets/projects/nhanes.jpg",
    year:"2026",
    field:"Public health, survival analysis",
    summary:"Followed 50,819 US adults in NHANES for death, using survey-weighted Cox models, competing risks and inverse probability weighting.",
    result:"Chronic kidney disease explained 14.7% of deaths, more than smoking.",
    intro:"A survey-weighted survival analysis of NHANES 1999 to 2018 linked to National Death Index mortality, with competing risks, causal inference, a 10-year risk model and a Power BI dashboard.",
    question:"How much do diabetes, prediabetes, hypertension, obesity and chronic kidney disease (CKD) raise the risk of death, what do people with them die of, and how much of all death can be put down to each one?",
    data:"50,819 US adults who had a full NHANES exam between 1999 and 2018, followed for death up to the end of 2019. 8,279 of them died over 479,971 person-years, with a median follow-up of 9 years.",
    tools:["R (survey, mice, survival)","Python","DuckDB SQL","Power BI"],
    findings:[
      {stat:"14.7%",title:"CKD carries the largest share of deaths",text:"Hazard ratio 1.59 (1.50 to 1.68). More deaths were attributable to CKD than to smoking (13.1%), hypertension (11.8%) or diabetes (8.3%)."},
      {stat:"HR 0.99",title:"Prediabetes looked dangerous, but the excess was age",text:"The crude death rate was 19.4 per 1,000 person-years against 10.8 with normal glucose. After full adjustment the hazard ratio was 0.99 (0.92 to 1.06)."},
      {stat:"HR 2.27",title:"Crude rates hid the risk of smoking",text:"Smokers in the sample were younger, so their crude death rate did not stand out. After adjustment, current smoking was the strongest single factor in the model."},
      {stat:"HR 1.44",title:"Diabetes raises the risk of death",text:"The total effect from inverse probability weighting was larger, HR 1.83, about 6.3 extra deaths per 100 people over 10 years. About 23.4% of all diabetes was undiagnosed."},
      {stat:"28.5%",title:"The usual shortcut overstates cause-specific risk",text:"Treating other causes of death as censored overstated the 15-year risk of a specific cause by up to 28.5%, compared with the Aalen-Johansen estimator."},
      {stat:"C-index 0.872",title:"10-year risk of death can be predicted well",text:"The model was trained on 1999 to 2006 and tested on 2007 to 2010. Observed risk was 10.4% against a predicted 10.2%."}
    ],
    methods:[
      "Built the cohort in Python and DuckDB SQL from 14 NHANES components across 10 survey cycles, with every exclusion counted.",
      "Applied the survey design (PSU, strata and weights) to every estimate with the R survey package.",
      "Handled missing values with multiple imputation in mice, 20 imputations, with the outcome in the imputation model.",
      "Fitted survey-weighted Cox models in three adjustment steps, with splines for age and lab values and six sensitivity analyses.",
      "Estimated cause-specific risk with the Aalen-Johansen estimator, cause-specific Cox models and Fine-Gray models.",
      "Estimated total effects with inverse probability weighting and E-values, and attributable fractions with Miettinen's formula.",
      "Built an 8-page Power BI dashboard that only displays the R results, so its numbers match the report exactly."
    ],
    shots:[
      {src:"assets/projects/nhanes/1.jpg",caption:"Executive summary"},
      {src:"assets/projects/nhanes/2.jpg",caption:"Survival and hazard ratios"},
      {src:"assets/projects/nhanes/3.jpg",caption:"Competing risks and causes of death"},
      {src:"assets/projects/nhanes/4.jpg",caption:"Causal effects and attributable burden"}
    ],
    links:[{label:"Read the full report",path:"NHANES%20Cardiometabolic%20Mortality%20Analysis%20Report.pdf"}]
  },
  {
    slug:"diabetes",
    title:"Diabetes 30-day hospital readmission",
    repo:"Diabetes-Readmission-Analysis-",
    image:"assets/projects/diabetes.jpg",
    year:"2026",
    field:"Public health, risk modelling",
    summary:"69,970 diabetic patients from 130 US hospitals. SQL questions, logistic regression, an XGBoost risk model with SHAP and an 8-page Power BI dashboard.",
    result:"3 or more prior inpatient stays: adjusted OR 3.61.",
    intro:"SQL, exploratory analysis, statistical inference, a risk model and a Power BI dashboard on diabetic patients from 130 US hospitals. About 1 in 11 came back to hospital within 30 days of discharge.",
    question:"Where is 30-day readmission concentrated, is measuring HbA1c during the stay linked to fewer readmissions once patient mix is adjusted for, and how well can readmission be predicted at discharge?",
    data:"69,970 patients from the UCI Diabetes 130-US Hospitals dataset (1999 to 2008), taking the first encounter per patient and removing hospice and death discharges. The 30-day readmission rate is 8.97%.",
    tools:["Python","DuckDB SQL","XGBoost","SHAP","Power BI"],
    findings:[
      {stat:"OR 3.61",title:"Prior inpatient stays are the strongest risk factor",text:"26.5% of patients with 3 or more prior inpatient stays were readmitted, against 8.1% with none. Adjusted odds ratio 3.61 (3.09 to 4.23)."},
      {stat:"OR 2.17",title:"Discharge destination comes second",text:"15.2% of patients transferred to another facility were readmitted, against 7.0% of those sent home."},
      {stat:"OR 0.96",title:"HbA1c testing shows no overall link",text:"Adjusted odds ratio 0.96 (0.89 to 1.03), and 0.99 after propensity score matching."},
      {stat:"p = 0.0067",title:"But the link depends on the diagnosis",text:"The interaction with primary diagnosis was significant. Testing went with lower odds for injury (OR 0.61), respiratory (0.76) and diabetes (0.81) admissions."},
      {stat:"18.4%",title:"HbA1c is rarely measured",text:"Only 18.4% of patients were tested during the stay, and only 35.9% even with a primary diabetes diagnosis."},
      {stat:"AUC 0.659",title:"The risk model is modest but well calibrated",text:"PR-AUC was 0.183 against a 0.090 baseline. The top 20% of patients by predicted risk hold 38% of all readmissions."}
    ],
    methods:[
      "Answered 13 business questions in DuckDB SQL with window functions and 95% Wilson confidence intervals.",
      "Ranked features by effect size instead of p-values, since with 70,000 patients almost every difference is significant.",
      "Fitted logistic regression for adjusted odds ratios, with a likelihood-ratio test for the HbA1c and diagnosis interaction.",
      "Checked the HbA1c result with 1:1 propensity score matching. The largest standardized mean difference fell from 0.307 to 0.037.",
      "Compared logistic regression with XGBoost on an 80/20 stratified split, tuned on PR-AUC, with the test set used once.",
      "Set the decision threshold from a cost ratio, explained the model with SHAP and scored every patient into risk tiers.",
      "Built an 8-page Power BI dashboard on a star schema with 158 DAX measures."
    ],
    shots:[
      {src:"assets/projects/diabetes/1.jpg",caption:"Executive summary"},
      {src:"assets/projects/diabetes/2.jpg",caption:"Readmission drivers"},
      {src:"assets/projects/diabetes/3.jpg",caption:"Statistical and model results"},
      {src:"assets/projects/diabetes/4.jpg",caption:"Risk tiers and what-if"}
    ],
    links:[{label:"Read the full report",path:"Diabetes%20Readmission%20Analysis%20Report.pdf"}]
  },
  {
    slug:"wind",
    title:"Monthly wind speed forecasting in Bangladesh",
    repo:"Bangladesh-wind-speed-forecasting",
    image:"assets/projects/wind.jpg",
    year:"2026",
    field:"Climate, time series forecasting",
    summary:"SARIMA against Random Forest, XGBoost, SVR, LSTM and a hybrid model on 43 years of NASA POWER data for 64 districts.",
    result:"No model was significantly better than SARIMA on Diebold-Mariano tests.",
    intro:"A comparison of a seasonal ARIMA model with five machine learning models on national monthly mean wind speed in Bangladesh, 1982 to 2024. This was my final-year research.",
    question:"Can machine learning models forecast monthly wind speed in Bangladesh better than a seasonal ARIMA model?",
    data:"The monthly mean of daily 10 m wind speed from NASA POWER, averaged over 64 district points. Models were trained on 492 months (1982 to 2022) and tested on a 24-month holdout (2023 to 2024).",
    tools:["R","Python","SARIMA","XGBoost","LSTM"],
    shotsTitle:"Figures",
    findings:[
      {stat:"0 of 5",title:"No model is significantly better than SARIMA",text:"Diebold-Mariano tests with Holm correction found no significant gain, on the holdout (n = 24) or on the pooled cross-validation forecasts (n = 120)."},
      {stat:"RMSE 0.236",title:"Random Forest had the lowest holdout error",text:"Its gap to SARIMA (0.247 m/s) is small and not significant. LSTM, XGBoost, the hybrid and SVR followed."},
      {stat:"MAPE 6.38%",title:"SARIMA had the lowest MAE and MAPE",text:"SARIMA(0,1,1)(0,1,1)[12] was chosen on the training data by BIC and has only two parameters."},
      {stat:"R² 0.82",title:"Cross-validation agrees with the holdout",text:"Over 5 rolling-origin folds of 24 months, Random Forest (R² 0.819) and SARIMA (0.817) stayed ahead of the other models."},
      {stat:"p = 0.0015",title:"SVR is significantly worse",text:"On the pooled cross-validation forecasts, support vector regression was the only model significantly different from SARIMA, and in the wrong direction."}
    ],
    methods:[
      "Aggregated daily NASA POWER files for 64 districts into a national monthly series in R.",
      "Selected the SARIMA order on the training data by BIC, with stationarity tests and residual diagnostics.",
      "Built 21 predictors for the machine learning models: lags, rolling statistics, month, weather covariates, and ENSO and IOD indices.",
      "Found and fixed a leakage error in the rolling features. They are now built after a one-month shift, scalers are fit on training rows only, and an audit stops the run if either rule is broken.",
      "Compared all six models on a 24-month holdout, 5-fold rolling-origin cross-validation and Diebold-Mariano tests."
    ],
    shots:[
      {src:"assets/projects/wind/1.jpg",caption:"Monthly mean wind speed and its distribution by calendar month"},
      {src:"assets/projects/wind/2.jpg",caption:"Holdout forecasts against observed values"},
      {src:"assets/projects/wind/3.jpg",caption:"Holdout and cross-validation RMSE by model"},
      {src:"assets/projects/wind/4.jpg",caption:"Diebold-Mariano test statistics against SARIMA"}
    ],
    links:[]
  },
  {
    slug:"dunnhumby",
    title:"Dunnhumby retail analytics",
    repo:"dunnhumby-retail-analytics",
    image:"assets/projects/dunnhumby.jpg",
    year:"2026",
    field:"Retail, causal inference",
    summary:"RFM segmentation, retention analysis and market basket analysis on 2,500 households, plus a causal test of campaign uplift.",
    result:"A naive uplift of $31.40 a week fell to $1.03 after matching.",
    intro:"Customer and campaign analysis of a grocery retailer using Dunnhumby's The Complete Journey dataset: who drives sales, how households lapse and come back, which products are bought together, and whether campaigns work.",
    question:"Did the retailer's marketing campaigns actually make households spend more?",
    data:"2,500 households, 2 years of grocery transactions and 30 marketing campaigns. Over 86 stable weeks, 2,493 households made 230,892 trips and spent $6.81M.",
    tools:["Python","DuckDB SQL","lifelines","statsmodels","Power BI"],
    findings:[
      {stat:"+$1.03",title:"The campaign effect almost disappears",text:"Targeted households spent $31.40 a week more than the rest. After matching and difference in differences, the effect was +$1.03 a week (95% CI -$0.99 to $3.05, p = 0.32)."},
      {stat:"50.5%",title:"Champions bring half of sales",text:"Champions are 23.8% of households but bring 50.5% of sales. 280 At risk households spend like Loyal ones but have not shopped for 33 days."},
      {stat:"98%",title:"Households lapse, then come back",text:"70% of households broke their normal shopping rhythm at least once, and 98% of them returned. Only 1.2% never came back."},
      {stat:"HR 0.78",title:"Broader shoppers break less often",text:"Households that buy from more departments lapse less often, with a hazard ratio of 0.78."},
      {stat:"Lift 16.4",title:"The strongest basket links are need-based",text:"Cat food and litter (lift 16.4), brooms or mops with cleaning products (11.6), and pasta with sauce (9.7, in 5,940 baskets)."}
    ],
    methods:[
      "Answered 12 questions a retail manager would ask in DuckDB SQL on Parquet files.",
      "Segmented households with RFM in SQL and checked the segments against k-means.",
      "Modelled retention with Kaplan-Meier and Cox models, using a lapse threshold set per household.",
      "Ran market basket analysis with a SQL self-join for support, confidence and lift.",
      "Estimated campaign impact with stacked difference in differences, propensity score matching, an event study and a placebo test.",
      "Built a 4-page Power BI dashboard on a star schema, with a recommendation on every page."
    ],
    shots:[
      {src:"assets/projects/dunnhumby/1.jpg",caption:"Store overview"},
      {src:"assets/projects/dunnhumby/2.jpg",caption:"Customers"},
      {src:"assets/projects/dunnhumby/3.jpg",caption:"Baskets"},
      {src:"assets/projects/dunnhumby/4.jpg",caption:"Campaigns"}
    ],
    links:[{label:"View the dashboard PDF",path:"outputs/dashboard/Dunnhumby_Dashboard.pdf"}]
  },
  {
    slug:"berka",
    title:"Berka retail banking analytics",
    repo:"Berka-banking-analytics",
    image:"assets/projects/berka.jpg",
    year:"2026",
    field:"Banking, data modelling",
    summary:"ETL pipeline and star schema over 1,056,320 transactions, feeding a 7-page Power BI dashboard with 77 DAX measures.",
    result:"Loans above 250K CZK defaulted at about 23%, against 7% under 100K.",
    intro:"End to end analytics on the Berka PKDD'99 Financial Dataset, from eight raw files to a seven-page Power BI dashboard. The point was to build the whole chain myself, not one part of it.",
    question:"What does a Czech bank's data show about deposits, cash flow and loan risk, once it is modelled properly from the raw files?",
    data:"1,056,320 transactions across 4,500 accounts of a Czech bank, 1993 to 1998, with 682 loans. The data comes as eight raw text files.",
    tools:["Python","DuckDB","SQL","Power BI (DAX, Power Query)"],
    findings:[
      {stat:"23%",title:"Loan size predicts default far better than loan term",text:"Loans under 100K CZK defaulted at about 7%, 100K to 250K at about 9%, and above 250K at about 23%. The overall default rate is 11.1%, 76 of 682 loans."},
      {title:"Right censoring made the first version misleading",text:"Loans issued late in the window had not had time to default. The model now reports the default rate and the matured-only default rate side by side."},
      {title:"Sanction interest is a symptom, not a predictor",text:"Accounts hit distress after origination, so using sanction interest as a credit signal would leak future information into a model."},
      {stat:"r ≈ 0.04",title:"Unemployment does not explain default at district level",text:"Measured across 65 districts with at least 5 loans each. A null result, but a real one."},
      {stat:"0.006%",title:"Two independent paths agree",text:"Cumulative net transaction flow and total closing balance for December 1998 differ by 0.006%. They are computed separately, so this is the main check that the pipeline is sound."}
    ],
    methods:[
      "Loaded the raw files as text, so every type decision is applied explicitly afterwards and is visible in the notebook.",
      "Built a star schema in DuckDB with six dimensions, one bridge and five fact tables, joined by 17 relationships.",
      "Derived tables for balance snapshots, the loan cohort, account behaviour and account distress.",
      "Built a 7-page Power BI dashboard with 77 DAX measures, including semi-additive balances and what-if parameters.",
      "Saved row count and missingness profiles at each stage as the checks the pipeline was validated against."
    ],
    shots:[
      {src:"assets/projects/berka/1.jpg",caption:"Executive overview"}
    ],
    links:[]
  },
  {
    slug:"olist",
    title:"Olist Brazilian e-commerce analytics",
    repo:"olist-ecommerce-analytics",
    image:"assets/projects/olist.jpg",
    year:"2026",
    field:"E-commerce, SQL",
    summary:"SQL-first analysis of 99,441 orders in DuckDB. Power BI only displays what the SQL already computed.",
    result:"Review score drops from 4.15 to 3.46 once an order is late.",
    intro:"A SQL-first analysis of the Olist marketplace. The cleaning, the dimensional model, the bucketing and the window functions all happen in DuckDB, and Power BI only displays the result.",
    question:"What drives review scores and revenue on a marketplace, and how much of it can be answered in SQL alone?",
    data:"99,441 orders from the Olist marketplace, September 2016 to August 2018. Results are on the 96,478 delivered orders.",
    tools:["DuckDB","SQL","Python","Power BI","LaTeX"],
    findings:[
      {stat:"4.15 to 3.46",title:"Late delivery breaks the review score at a threshold",text:"The score barely moves while orders are early, then falls to 3.46 at 0 to 5 days late and 1.89 at 5 to 10 days late. The share of 1 and 2 star reviews goes from 11.07% to 73.81%."},
      {stat:"91.9%",title:"The on-time rate comes from padding, not speed",text:"Olist adds 8 to 19 days of buffer to the delivery estimate shown at checkout. Average delay is negative in all 27 states."},
      {stat:"3.00%",title:"There is almost no retention",text:"Of 93,358 unique customers, 3.00% ordered more than once. Repeat customers are worth 1.87 times more, but there are very few of them."},
      {stat:"133 sellers",title:"Revenue is concentrated",text:"133 of 2,970 sellers make half the revenue, and the state of São Paulo alone is 37.4%."},
      {stat:"R$145 to R$175",title:"Growth was volume, not basket size",text:"Monthly orders went from about 750 to 6,500, while average order value stayed in the same band for the whole 24 months."}
    ],
    methods:[
      "Loaded nine CSVs into a raw schema as text, then typed and cleaned them in a staging layer.",
      "Built a fact constellation in DuckDB with 4 fact tables and 5 conformed dimensions.",
      "Answered 10 analytical questions, all with window functions.",
      "Keyed all customer analysis on customer_unique_id, since customer_id is issued new for every order.",
      "Exported 10 BI views to Parquet for a 4-page Power BI dashboard.",
      "Wrote the full report in LaTeX."
    ],
    shots:[
      {src:"assets/projects/olist/1.jpg",caption:"Executive overview"},
      {src:"assets/projects/olist/2.jpg",caption:"Geography"},
      {src:"assets/projects/olist/3.jpg",caption:"Delivery and satisfaction"},
      {src:"assets/projects/olist/4.jpg",caption:"Customers and sellers"}
    ],
    links:[{label:"Read the full report",path:"report/Olist_Step07_Report.pdf"}]
  }
];
const POSTS=[
];
