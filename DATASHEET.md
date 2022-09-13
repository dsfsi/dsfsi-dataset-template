# Datasheet: Vukuzenzele-nlp

Author: *Your Name Here*

Organization: Data Science for Social Impact Research Group (DSFSI)


## Motivation

*The questions in this section are primarily intended to encourage dataset creators to clearly articulate their reasons for creating the dataset and to promote transparency about funding interests.*

1. **For what purpose was the dataset created?** Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

	The dataset was created to obtain translated text in all 11 official languages in South Africa. The text was obained from the vukuzenzele news articles that contain translated stories in each of the 11 languages.

2. **Who created this dataset (e.g. which team, research group) and on behalf of which entity (e.g. company, institution, organization)**?

	The DSFSI group at the University of Pretoria.

3. **What support was needed to make this dataset?** (e.g. who funded the creation of the dataset? If there is an associated grant, provide the name of the grantor and the grant name and number, or if it was supported by a company or government agency, give those details.)

	The University of Pretoria.

4. **Any other comments?**

	The translated text taken from the Vukuzenzele articles, has each edition processed individually.


## Composition

*Dataset creators should read through the questions in this section prior to any data collection and then provide answers once collection is complete. Most of these questions are intended to provide dataset consumers with the information they need to make informed decisions about using the dataset for specific tasks. The answers to some of these questions reveal information about compliance with the EU’s General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions.*

1. **What do the instances that comprise the dataset represent (e.g. documents, photos, people, countries)?** Are there multiple types of instances (e.g. movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.


	The dataset comprises of text documents in the form of pdfs and txt files.

	The data set comprises of: 
	a. The pdf versions of the vukuzenzele newsletter.
	b. Interim and processed text files.

2. **How many instances are there in total (of each type, if appropriate)?**

	There are three sets: 
	a. The raw (pdf)
	b. interim (txt) 
	c. processed (txt) 
	The files are subject to continous change hence a specfic number of each cannot be stated. 

3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g. geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g. to cover a more diverse range of instances, because instances were withheld or unavailable).

	The dataset contains all the possible instances of papers (raw-pdf data) containing 11 translations of the vukuzenzele articles currently available.
	The interim and processed text files contain common stories from the articles in the raw pdfs. 

4. **What data does each instance consist of?** "Raw" data (e.g. unprocessed text or images) or features? In either case, please provide a description.

	a. Raw data - unprocessed text in pdf files of articles from 2012-11-ed1 to 2022-07-ed2.
	b. Interim data - extracted text of common stories obtained from raw data. Each story has 11 files, 1 story in each of the 11 languages.  
	c. Processed data - processed individual stories text from the interim data. 

5. **Is there a label or target associated with each instance?** If so, please provide a description.

	a. Raw data - unprocessed text stories.
	b. Interim - Extract text stories.
	c. Processed - Processed text stories.

6. **Is any information missing from individual instances?** If so, please provide a description, explaining why this information is missing (e.g. because it was unavailable). This does not include intentionally removed information, but might include, e.g. redacted text.

	a. There are missing pdfs for other languages in raw data as these were unavailable: 2022-03-ed2, 2015-08-ed1, and 2015-04-ed1. The specific files have been docouented in each respective folder. 
	b. From 2012-10-ed1 to 2005, there are no available PDFs for the raw data. These are unavailable from the source.
	c. The interim and processed files still have stories that need to be evaluated therefore there is data still to be obtained.

7. **Are relationships between individual instances made explicit (e.g. users' movie ratings, social network links)?** If so, please describe how these relationships are made explicit.

	Common stories. There are common stories in each of the pdfs in the raw data. 
	There are a number of stories in each edition that have been translated over the 11 official languages.
	These stories are then extracted and processed into individual text files containing each story in a specific langauage.   

8. **Are there recommended data splits (e.g. training, development/validation, testing)?** If so, please provide a description of these splits, explaining the rationale behind them.

	There is raw data, interim and processed data. The splits are a representation of what stage of evaluation the files are on in order to be able to trace the data flow from start to finish.

9. **Are there any errors, sources of noise, or redundancies in the dataset?** If so, please provide a description.

	The extraction of stories varies between editions hence there is alot of data that requires human intervention as opposed to the automated extraction hope for.

10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g. websites, tweets, other datasets)?** If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g. licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.

	The dataset was obtain from the vukuzenzele archives website hence it depends on the updates made to the website in order to increase the database. Once the pdf raw data has been obtained, the dataset is then self-contained. 

11. **Does the dataset contain data that might be considered confidential (e.g. data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** If so, please provide a description.

	The dataset is not confidential or have any known access restrictions.

12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** If so, please describe why.

	The dataset contains data which may be viewed as such. The data is of story articles which have been documented and distributed to the public as vukuzenzele is a newsletter that consistently writes on relevant issues that are occuring hence there may be text that is offensive, insulting, threating or that which may cause anxiety depending on the stance of the observer. 

13. **Does the dataset relate to people?** If not, you may skip the remaining questions in this section.

	Yes, it relates to people.

14. **Does the dataset identify any subpopulations (e.g. by age, gender)?** If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.

	Yes, by language. The dataset contains articles on various topics that may related to different demographics. The text data is in the 11 official languages in South Africa therefore the groups that understand these specific languages. 

15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** If so, please describe how.

	Yes, within the data, it is possible to identify real person(s) although the main possess it to obtain translated story articles and not data on individuals.

16. **Does the dataset contain data that might be considered sensitive in any way (e.g. data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** If so, please provide a description.

	Yes, Vukuzenzele is a newsletter that provides story articles on various topics and overall content that may also be considered sensitive. 

17. **Any other comments?**

	


## Collection

*As with the previous section, dataset creators should read through these questions prior to any data collection to flag potential issues and then provide answers once collection is complete. In addition to the goals of the prior section, the answers to questions here may provide information that allow others to reconstruct the dataset without access to it.*

1. **How was the data associated with each instance acquired?** Was the data directly observable (e.g. raw text, movie ratings), reported by subjects (e.g. survey responses), or indirectly inferred/derived from other data (e.g. part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.

	The raw data was obsevable text in pdf files, with each article story separeted either through the pages. The interim data was extracted using a script (vukuzenzele-extract.py) according to a number of factors including but not limited to: page breaks, paragraph spacing, and page numbers. The processed data includes data that has been verified and validated by an individual. The person would identify errors within the extracted text and organise and retify the errors. 

2. **What mechanisms or procedures were used to collect the data (e.g. hardware apparatus or sensor, manual human curation, software program, software API)?** How were these mechanisms or procedures validated?

	A python script (vukuzenzele-extract) was used to extracted texted data from the raw data (pdf files). The script was tested and evaluated on different instances of the raw data to validate its functionality. 

3. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g. deterministic, probabilistic with specific sampling probabilities)?**

	The dataset is the complete dataset and not a sample. The dataset only contains instances where pdf files were available for each edition at a given date. The was no sampling strategy used.

4. **Who was involved in the data collection process (e.g. students, crowdworkers, contractors) and how were they compensated (e.g. how much were crowdworkers paid)?**

	A winter research assistant.

5. **Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (e.g. recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. Finally, list when the dataset was first published.

	The data was collected during the July 2022 period.

7. **Were any ethical review processes conducted (e.g. by an institutional review board)?** If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.

	The tasks relevent to the data were oversean and reviewed by members in the Data Science for Social Impact Research Group (DSFSI).  

8. **Does the dataset relate to people?** If not, you may skip the remainder of the questions in this section.

	No, it does not.

9. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g. websites)?**

	*Your Answer Here*

10. **Were the individuals in question notified about the data collection?** If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.

	*Your Answer Here*

11. **Did the individuals in question consent to the collection and use of their data?** If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.

	*Your Answer Here*

12. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).

	*Your Answer Here*

13. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g. a data protection impact analysis) been conducted?** If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.

	*Your Answer Here*

14. **Any other comments?**

	*Your Answer Here*


## Preprocessing / Cleaning / Labeling

*Dataset creators should read through these questions prior to any pre-processing, cleaning, or labeling and then provide answers once these tasks are complete. The questions in this section are intended to provide dataset consumers with the information they need to determine whether the “raw” data has been processed in ways that are compatible with their chosen tasks. For example, text that has been converted into a “bag-of-words” is not suitable for tasks involving word order.*

1. **Was any preprocessing/cleaning/labeling of the data done (e.g. discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** If so, please provide a description. If not, you may skip the remainder of the questions in this section.

	The following applies to the sections listed:
	Raw data:
		a. Common stories were extracted from the pdf in each edition and sent to interim data.
		b. The vukuzenzele-extract.py python script is used for extraction.
	Interim data:
		a. Extracted stories were assigned a story number and the language of each story using a specific naming convention
		b. The stories were then manually formated in order to extract the title, author and story only.
		c. The stories are then sent to the processed data. 

2. **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g. to support unanticipated future uses)?** If so, please provide a link or other access point to the "raw" data.

	Yes. The raw data was saved and remains unedited throughout. 

3. **Is the software used to preprocess/clean/label the instances available?** If so, please provide a link or other access point.

	A python script: vukuzenzele-extract.py

4. **Any other comments?**

	Naming convention of interim and processed data:

		Year-Month-Edition-PaperName-articleNo-Language
		YYYY-MM-edN-vukuzenzele-CCC-AAA


## Uses

*These questions are intended to encourage dataset creators to reflect on the tasks  for  which  the  dataset  should  and  should  not  be  used.  By  explicitly highlighting these tasks, dataset creators can help dataset consumers to make informed decisions, thereby avoiding potential risks or harms.*

1. **Has the dataset been used for any tasks already?** If so, please provide a description.

	*Your Answer Here*

2. **Is there a repository that links to any or all papers or systems that use the dataset?** If so, please provide a link or other access point.

	A github repository: https://github.com/dsfsi/vukuzenzele-nlp

3. **What (other) tasks could the dataset be used for?**

	*Your Answer Here*

4. **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g. stereotyping, quality of service issues) or other undesirable harms (e.g. financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?

	The dataset has no aspects that may impact future uses aside from the extraction process, which may not always be efficient hence a README.md file has been created on how the extraction process is done and all the limitations a user may encounter while using it and the dataset.

5. **Are there tasks for which the dataset should not be used?** If so, please provide a description.

	*Your Answer Here*

6. **Any other comments?**

	*Your Answer Here*


## Distribution

*Dataset creators should provide answers to these questions prior to distributing the dataset either internally within the entity on behalf of which the dataset was created or externally to third parties.*

1. **Will the dataset be distributed to third parties outside of the entity (e.g. company, institution, organization) on behalf of which the dataset was created?** If so, please provide a description.

	*Your Answer Here*

2. **How will the dataset will be distributed (e.g. tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

	*Your Answer Here*

3. **When will the dataset be distributed?**

	*Your Answer Here*

4. **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.

	*Your Answer Here*

5. **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.

	*Your Answer Here*

6. **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.

	*Your Answer Here*

7. **Any other comments?**

	*Your Answer Here*


## Maintenance

*As with the previous section, dataset creators should provide answers to these questions prior to distributing the dataset. These questions are intended to encourage dataset creators to plan for dataset maintenance and communicate this plan with dataset consumers.*

1. **Who is supporting/hosting/maintaining the dataset?**

	The Data Science for Social Impact Research Group (DSFSI)

2. **How can the owner/curator/manager of the dataset be contacted (e.g. email address)?**

	Email: vukosi.marivate@cs.up.ac.za

3. **Is there an erratum?** If so, please provide a link or other access point.

	None.

4. **Will the dataset be updated (e.g. to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to users (e.g. mailing list, GitHub)?

	Yes. The interim and processed data will constantly be updated with new instances of common stories and subsequent processed text files with no specific timeframe or rate of change. The updates will then be uploaded to the Github repository. The DSFSI group will update and communicate updates internally.

5. **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g. were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** If so, please describe these limits and explain how they will be enforced.

	No. It does not related to people.

6. **Will older versions of the dataset continue to be supported/hosted/maintained?** If so, please describe how. If not, please describe how its obsolescence will be communicated to users.

	The dataset is constantly updated hence there will be no previous versions. The github repository will be overriden with new data and only reverted if there are any errors that have been identified. This will be communicated through github.

7. **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.

	The github repository is used for contributions and the DSFSI group overseas the approval of contributions. They validate and verify the contributions. The github pull requests and provided form of communication on the site can be used for any clarification and notification purposes.  

8. **Any other comments?**

	
