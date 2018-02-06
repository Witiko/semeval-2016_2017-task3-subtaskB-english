"""This module provides preprocessing routines for SemEval Task 3, Subtask B datasets."""

from lxml import etree

def parse(xmlfile):
    tree = etree.parse(xmlfile)
    orgquestions = []
    seen_orgquestion_ids = set()
    for orgquestion in tree.findall("OrgQuestion"):
        if orgquestion.attrib["ORGQ_ID"] in seen_orgquestion_ids:
            continue
        seen_orgquestion_ids.update([orgquestion.attrib["ORGQ_ID"]])
        threads = []
        for thread in tree.findall(
                "OrgQuestion[@ORGQ_ID='%s']/Thread" % orgquestion.attrib["ORGQ_ID"]):
            relquestion = {}
            for attrib in (
                    "RELQ_ID", "RELQ_CATEGORY", "RELQ_DATE",
                    "RELQ_USERID", "RELQ_USERNAME", "RELQ_RELEVANCE2ORGQ"):
                relquestion[attrib] = thread.find("RelQuestion").attrib[attrib]
            relquestion["RELQ_RANKING_ORDER"] = \
                int(thread.find("RelQuestion").attrib["RELQ_RANKING_ORDER"])
            relquestion["RelQSubject"] = thread.find("RelQuestion/RelQSubject").text or ""
            relquestion["RelQBody"] = thread.find("RelQuestion/RelQBody").text or ""

            relcomments = []
            for i, relcomment in enumerate(thread.findall("RelComment")):
                relcomments.append({})
                for attrib in (
                        "RELC_ID", "RELC_DATE", "RELC_USERID", "RELC_USERNAME",
                        "RELC_RELEVANCE2ORGQ", "RELC_RELEVANCE2RELQ"):
                    relcomments[i][attrib] = relcomment.attrib[attrib]
                relcomments[i]["RelCText"] = relcomment.find("RelCText").text or ""

            threads.append({
                "THREAD_SEQUENCE": thread.attrib["THREAD_SEQUENCE"],
                "RelQuestion": relquestion,
                "RelComments": relcomments})
        orgquestions.append({
            "ORGQ_ID": orgquestion.attrib["ORGQ_ID"],
            "OrgQSubject": orgquestion.find("OrgQSubject").text or "",
            "OrgQBody": orgquestion.find("OrgQBody").text or "",
            "Threads": threads})
    return orgquestions
