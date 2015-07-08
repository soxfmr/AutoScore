# -*- coding: utf-8 -*-
import urllib, urllib2

_LOGIN_COOKIE = ''

def HttpRequest(url, params = ''):
        if params != '':
                params = urllib.urlencode(params)
                req = urllib2.Request(url, params)
        else:
                req = urllib2.Request(url)

        # 添加Header 或者 Cookies
        global _LOGIN_COOKIE
        req.add_header('Cookie', _LOGIN_COOKIE)

        res = urllib2.urlopen(req)
        result = res.read()
        return result

def setScore(teacherId):
        params = {
                'DdXq':'2014/2015(2)',
                'BCpKc':teacherId,
                'DF44':'8',
                'BZ':'100.0',
                'DF46':'8',
                'DF47':'8',
                'DF72':'6',
                'DF43':'5',
                'DF55':'5',
                'DF60':'5',
                'DF59':'7',
                'DF61':'10',
                'DF74':'8',
                'DF179':'6',
                'DF180':'6',
                'DF45':'6',
                'DF56':'6',
                'DF73':'6',
                'DF178':'0',
                'DF181':'0',
                'DF182':'0',
                'SaveD':'1',
                'cDdXq':'2014/2015(2)',
                'cBKcCode':teacherId,
                'cBKcText':'大学生心理健康教育<齐力><未评>',
                'PjXx':'亲爱的同学，你对老师的真实评价可以促进老师提高教学质量，也使母校能够了解每位教师的教学情况，所以，请实事求是地给每位老师做出评价，如果有老师变相拉分可在扣分项（有悖师德的言行）打负分，谢谢你！',
                'pageId':'301601',
                'Xh':'141804004',
                'actionId':'register'}
        result = HttpRequest('http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet', params)

        return result

def setScoreByList(teacherList):
        if len(teacherList) > 0:
                print 'Get start to marking...'
                for teacher in teacherList:
                        print 'Give a mark to ' + teacher + '...'
                        setScore(teacher)

                print 'All done! Now you should log-in to the system and then confirm all of the score to the server.'
        else:
                'The list of teacher is empty!'

def getTeacherList(data):
        Ret = []
        
        # 教师ID列表起始关键字
        firstKw = '<option value="0">-请选择-</option>'
        # 每个教师ID前缀关键字
        eachKw = '<option value='
        # 结束关键字
        endOfEachKw = ' >'
        # 待清理关键词，防止遍历出错
        killKw = ' selected'

        endOffset = 0

        firstKwLen = len(firstKw)
        eachKwLen = len(eachKw)
        endOfEachKwLen = len(endOfEachKw)

        index = data.find(firstKw)
        if index == -1:
                return Ret
        
        data = data[index + firstKwLen:]
        # 清理数据
        data = data.replace(killKw, ' ');

        index = data.find(eachKw)
        while(index != -1):
                index += eachKwLen
                endOffset = data.find(endOfEachKw)
                
                print 'Found Teacher ID: ' + data[index:endOffset]
                Ret.append(data[index:endOffset])

                endOffset += endOfEachKwLen
                data = data[endOffset:]

                index = data.find(eachKw)

        return Ret

#---------------------- Main ----------------------
print '============================================'
print '             Auto-Score by Yuge             '
print '              ver 0.1 20150630              '
print '============================================'

_LOGIN_COOKIE = raw_input('登录 Cookies：')

print 'Request data form website...'
# 获取教师列表
data = HttpRequest('http://jwxt.jmpt.cn:8125/JspHelloWorld/StdPjCz.jsp')
teacherList = getTeacherList(data)
# 开始评教
setScoreByList(teacherList)
