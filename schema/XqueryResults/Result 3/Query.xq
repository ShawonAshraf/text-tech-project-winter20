(: This query returns the old Tweets that we have obtained :)
/Tweets/Tweet[translate(created, "-:T", "") > translate("2020-12-30T00:00:00", "-:T", "")
and translate(created, "-:T", "") < translate("2021-01-05T00:00:00", "-:T", "")]