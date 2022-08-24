import aiohttp
import asyncio
import re

Headers = {
    "origin": "https://leetcode-cn.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}


async def get_leetcode_daily() -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("https://leetcode-cn.com/graphql", json={"operationName": "questionOfToday", "variables": {}, "query": "query questionOfToday { todayRecord {   question {     questionFrontendId     questionTitleSlug     __typename   }   lastSubmission {     id     __typename   }   date   userStatus   __typename }}"}, headers=Headers, timeout=5) as response:
                RawData = await response.json(content_type=None)
                EnglishTitle = RawData["data"]["todayRecord"][0]["question"]["questionTitleSlug"]
                QuestionUrl = f"https://leetcode-cn.com/problems/{EnglishTitle}"
            async with session.post("https://leetcode-cn.com/graphql", json={"operationName": "questionData", "variables": {"titleSlug": EnglishTitle}, "query": "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    langToValidPlayground    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    envInfo    book {      id      bookName      pressName      source      shortDescription      fullDescription      bookImgUrl      pressImgUrl      productUrl      __typename    }    isSubscribed    isDailyQuestion    dailyRecordStatus    editorType    ugcQuestionId    style    __typename  }}"}, headers=Headers, timeout=5) as response:
                RawData = await response.json(content_type=None)
                Data = RawData["data"]["question"]
                ID = Data["questionFrontendId"]
                Difficulty = Data["difficulty"]
                ChineseTitle = Data["translatedTitle"]
                Content = re.sub(r"(<\w+>|</\w+>)", "", Data["translatedContent"]).replace("&nbsp;", "").replace("&lt;", "<").replace("\t", "").replace("\n\n", "\n").replace("\n\n", "\n")
                Data = {"id": ID, "title": ChineseTitle, "difficulty": Difficulty, "content": Content, "url": QuestionUrl}
                return Data
    except:
        return "获取信息失败"
