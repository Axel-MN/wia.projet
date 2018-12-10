For non-medical questions:

Multiple NIST assessors independently created question interpretations
and judged responses for the set of non-medical questions.  (We asked
assessors to provide their own paraphrase of the question both to see
how the assessor was interpreting the question and to provide future
training data for systems.) The number of assessors per question varies,
depending on how many questions an assessor could get to in the
allotted assessing time.  Each question (except questions 7760 and 7917
that are not in English and were therefore dropped), had a primary
assessor who was assigned the question first.  Only the primary assessor's
judgment is available on the web site, and only the judgment was used in scoring. 


The file qids.txt  gives the mapping between external (Yahoo) question ID and
the NIST-assigned id.  It is of the form
	NIST-id Yahoo-id

The file 'anon-qrels.txt' contains the assessments from the primary assessor.
The file is in the
	 form qid judgment response
where qid is the NIST-assigned id for the question.  The scale for judgments
is 1: Bad
   2: Okay
   3: Good
   4: Excellent
  -2: Unintelligible
Responses are the strings as returned by the system with all new line
characters translated into spaces.  Note that there are duplicate
response-strings in this file which happens when two different systems
return identical strings.  Since assessors also saw each instance of 
duplicate response-strings, it is possible for different instances of
the same response-string to have different judgments (if the assessor were
inconsistent).

The file 'questionParaphrases.xml' contains the question interpretations
from all assessors who provided interpretations for that question.  This file
contains the text of the original question, the interpretation from the
primary assessor, and then the interpretations from all secondary
assessors.  Each interpretation is tagged with the assessor id of the
assessor who created it.  Through the assessor id, you can trace back
the judgments to the specific question interpretation.

For medical questions:

NIST assessors are not medical experts.  To judge the set of medical questions,
a NIST assessor was given a set of reference answers from a physician and
judged system responses based on the reference answers. Each medical question
has only one assessor.  The question interpretation for medical questions
was highly influenced by the reference answers.  Medical questions 10 and 103
did not make it into the question stream, so there are 102 medical questions judged.

The file 'med-qs-and-reference-answers.xml' is the set of questions together
with the corresponding reference answers for each question.

The file 'med-interpretations.xml' is the question interpretations for the
medical questions.

The file 'med-anon-qrels.txt' is the judgment file for the medical questions.

