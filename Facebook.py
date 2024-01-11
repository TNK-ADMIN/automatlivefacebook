import requests, json, re, base64, uuid, random, os
from urllib.parse import (parse_qsl, urlsplit)
from codecs import unicode_escape_decode
from bs4 import BeautifulSoup as bs

class FacebookProfile:
    NORMAL = "Profile"
    PRO5   = "Plus"
class FacebookReaction:
    LIKE    = 1635855486666999
    LOVE    = 1678524932434102
    CARE    = 613557422527858
    HAHA    = 115940658764963
    WOW     = 478547315650144
    SAD     = 908563459236466
    ANGRY   = 444813342392137

class FacebookMain:

    def __init__(self, proxy: str = None) -> None:
        self.__client           = requests.Session()
        if proxy != None and ':' in proxy:
            proxies = {
                'http': '',
                'https': ''
            }
            proxy = proxy.strip().split(':')
            if len(proxy) > 2: proxynew = f"http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
            else: proxynew = f"http://{proxy[0]}:{proxy[1]}"
            for x in proxies:
                proxies[x] = proxynew
            self.__client.proxies = proxies
        self.__client.headers       = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'referer': 'https://www.facebook.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }
        self.__client.headers ={
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.109", "Google Chrome";v="120.0.6099.109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'viewport-width': '2814',
        }
    def addCookie(self, cookie: str = ''):
        try:
            self.__client.headers['cookie'] = cookie
            self.cookie = cookie
            return self.infoAccount()
        except Exception as e: print(e)
        return False, "Cookie die"

    def check_url(self):
        send = self.__client.get('https://www.facebook.com/')
        print(send.status_code)
        open('a.html', 'w+', encoding='utf-8').write(send.text)
        url = send.url
        if '/login' in url: return False, "Cookie die"
        elif '/checkpoint' in url: 
            type_cp = None
            for pt in url.split('/'):
                try:
                    int(pt)
                    if pt[-3:] in ['282', '956']:
                        type_cp = pt[-3:]
                except: pass
            return False, "Tài khoản bị checkpoint" + ("|"+type_cp if type_cp != None else '')
        else: 
            return True, True
    
    def check_login_is_run(self):
        try:
            check_status = self.check_url()
            if check_status[0] == True: 
                return True, ''
            else: return check_status
        except: pass    
        return False, ''
    
    def infoAccount(self):
        try:
            send = self.__client.get('https://www.facebook.com/').text
            DTSG__INIT__ = re.findall('DTSGInitialData",\[\],{"token":"(.*?)"}', send)[0]
            if DTSG__INIT__:
                self.fb_dtsg = DTSG__INIT__
                self.jazoest = re.findall('&jazoest=(.*?)"', send)[0]
                self.idFacebook = str(re.findall('"USER_ID":"(.*?)"', send)[0])
                self.lsdFacebook = re.findall('\["LSD",\[\],{"token":"(.*?)"}', send)[0]
                self.nameFacebook = unicode_escape_decode(re.findall('"NAME":"(.*?)"', send)[0])[0]
                self.__client.headers['sec-fetch-site'] = 'same-origin'
                return True, {'idFacebook': self.idFacebook, 'nameFacebook': self.nameFacebook}
        except Exception as e:
            pass
        return False, "Cookie die"
    
    def __fectData(self, variables: str, doc_id: str) -> None or dict:
        return {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'lsd': self.lsdFacebook,
            'variables': variables,
            'server_timestamps': 'true',
            'doc_id': doc_id,
        }
    
    def follow(self, idProfile: str = ''):
        try: 
            res = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1696339372749,943159,250100865708545,","subscribe_location":"PROFILE","subscribee_id":"%s","actor_id":"%s","client_mutation_id":"1"},"scale":1.5}'%(idProfile, self.idFacebook), '6586385648082210')).json()
            if 'Đang theo dõi' in str(res) or 'Following' in str(res): return True, "Follow thành công"
            print(res)
        except: pass
        return False, "Thất bại"

    def reaction(self, idPost: str, typeReaction: FacebookReaction):
        try: 
            feed_id = base64.b64encode("feedback:{}".format(idPost).encode('utf-8')).decode('utf-8')
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,unexpected,1696387936457,498118,,;CometHomeRoot.react,comet.home,logo,1696387932844,919135,4748854339,229#230#301","feedback_id":"%s","feedback_reaction_id":"%s","feedback_source":"OBJECT","feedback_referrer":"/watch/","is_tracking_encrypted":true,"tracking":["AZV6rkakucGMIhae6j59YFq3is05VICnmDWyLqj7bI_XqebuKaMxLE9EvjBRwvwYGaWjAyJMXyq3j-0YuUzEF4DzLfNW8582SMRBXZ1eIGt9bxm1zxE0KZy0G9q2emZ4-Qx2L74kDZ6BHVFPTp3DednUJOq7sk1DPkuinvfnq2DVnL9j7hjcRRNg15otUpPN9ArCIdiQgO0XLSJnrgvZbq-lNL1NZyRzGrQsfV4D4dlsxrPt3kHQZKP3nkSqgL3ljeR_PcK2zFcyaFiHH1TiXNMcqp-XJufbo2b45ySYsdNRpqSUQUeopMwGMV_jHRSzHax5EEBTeEg_HtwsCnpmCt_ZGyaKCg0i9RXpiyl9YsJgDNIYxhrWXfE-xlhbAYs2EbrclElXNAmj-91QXJOwqkZPcQgJKL7OVqrNgCBtw3k9gfMX4FMRCyBoGBZA-uJSHBVNwYOb63OD0XXDN_KdV9FcxOdKWaQGTCBiy7loWxMv40Tds05Z559tMQvehTY25BdzbUEKZ1joOyZjMxABC3Vdk-JiOEebUBzmTXWLjoMmnkb03SR4guJhUlCQm5UEL6KZao3KsjXTT3bG941QeFzMYv6gJg7_9p8_iLOj0U9xbDtLRgiG0ooY9rTEDBU8K4IcSOR31IXckR0iEF1TYoUNniH7jmXzb5J1Zgncy2usWpVAGwzXyYkEvDSqj3_tdbLRo-3aKD4-aiw9pLiKnjZlQGXlbSSAFRY4se9FKCV62JRxvjua8MBLGS3YAdnyrMkacTUM48rTXvKE7vmWPjZQMZMN9z7CgRUHzHZKUWXR_oQoH8rvb5tgGoqWqDwy9Kgzy5p9bSx-bsTNkc7pyFyYjabqVIqPTUkm800SOdok4nywrx6Ql0aR-LgRKGXlMnM00uy4YhaqHYfgURr_gC90xJmJEJf2vjm2oVXw6IDf_k7zBJyWhdvKywHFCFuvG3YM_jkfRWH5ki5VyUPxUBF_wLi9NI3IBRQyliuamX8KbUJMktwM11VLGy_wR1rRozUdBe6D_uZxs-L__4PkR0a-szYj4lEQG7UK8Uzm5DmRbinFHTWSm7PM2HMiGM5bqNTBbK5WESG0xh-5gNY9dW_Bo02VhmX-CoMHPf2BoTGbRu0lB2WElfpMEaGcSb_NvQaOIJD3lgVhObetSnDFKjrcc4wDINMdUa6d4QhCadIidlE67LMDVwzxGI2wiK8AHuA"],"session_id":"58f2722b-5bf4-4896-b551-af63153b2103","actor_id":"%s","client_mutation_id":"4"},"useDefaultActor":false,"scale":1.5}'%(str(feed_id), typeReaction, self.idFacebook), '6324189467690403')).json()
            d = response['data']['feedback_react']['feedback']['can_viewer_react']
            return d, "Send reaction" + str('thành công' if d == True else 'thất bại')
        except Exception as e: print(e)
        return False, "Thất bại"

    def comment(self, idPost: str, textComment: str):
        try:
            feed_id = base64.b64encode("feedback:{}".format(idPost).encode('utf-8')).decode('utf-8')
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"groupID":null,"includeNestedComments":false,"input":{"attachments":null,"feedback_id":"%s","formatting_style":null,"message":{"ranges":[],"text":"%s"},"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1696422363149,451289,190055527696468,","is_tracking_encrypted":true,"tracking":["AZV37wK_b2uItR2_2MHHPDVFfwHQc_MFzG9t26zFGgJUb3mqonVmgkwoPX-MbUm7VJNZfjS3ehecfREMdw81J5Hy9d8LKsyX-GbBWcR0eeYKRj3dE9cPkLvET7q7cFYsTKUemLk0k9qlQEkjGD-Rxc0G9tvelqX46hSCK_pe6GwrMJ_lllccl_kpkUVL-BDPbcJ2VRJLVeehnYhfgS5C_af2mVuNNTk8gwsbJmVh-If8hqPGrKuPezhYDXnxkHOhhTEiRUVsUNW2WA2c2vOIhBjW0vdd1ERPptn03u-HnKLwhEbK8m8jBMfD9vCe0N1-DgsUmtrtGbPyxB1mYsPJapPYsPno6nQSfOyOSD2UglAVZrnhTlK6-Bw-LoJaW4R6XnoolIFzTKBm0JKIrPTBtu472xsQJmI4il6MtSBK1Gv2NmaUnAhCm5GOMbTqutEPK0uFBQWOQvS32TqABf_3KP3RtnYel8cMmNmKVM_7BlxEX8a2hdZbpZLua82ydNFF5eO7q7oIVmnwk2aicLkvuj9Xjix8YETglpeGaIAWpoERG4lEhNeXDV9EFhB1UHHXaIoFt5lOkvmDWMS8Tpum-BU-NmbPmicnlpwDL2b_MNcseHvP7fxaqSkgL8UVdAYFfwKtv1mBAUYR2iHLG_c6FLDmlOYgk7Wxm7PPYdfNu1lRjTSzLSGwpVOMJ5UAJoauqQEELRmlq_JXDRQqCJd2kPGUAnXIGqXYJXXrXlF56c-sDqejgtZh22reSryNx0wr1AZnsy5NCDCrQEK3QM0Ci2zc0Lpp77i3RP5xisquNg4u8jYE3SqhmM5GvG4nTGr_wXkqXH1TvTMoqAg5QFu3SRe6dE2j4LMsGHws9R8rLEGVFtTBZTb0o_KnkqF7Plm9u4ycz5d-E1cIwtk_dBC7JsMAC4RcNQ60oe1l_LUBoCdBv_e-9SSIZaQtPeP6cd4N_5hEcI5RfWehHmn2SzBayYm0To6Cn0dWDrQe7_i4U5oL9_Nf6lXAIVK--qdHC0yYIDLBPK4vDwunTbvhSpE1rXXCxsKDqIuibd0rzC-6dY1cMl0LBTV2mToS9Ur_hUi8dkNmo7aq-5rKDEQctsI-yU9fo__x8UkOkj57WmCu45RckqjKxF0QzPb86PMwX7kRrznU88pLeTWsD6FNMgW2-h2ha7csKT6gpsYcDHAQb1OnMnJ7qkw84KyPT7QPgUFl2YBYyeaAVGYSZ8uK8fuyl4x1lomqP9Uh086NzUwtHTbxw3dmyP7NucCPYN02WyeYVvleIlTZnXpunCRNIrNyPLyFb7s8_wcdOmZaNQK2SOgxIdH8aq_uFdh5OYmBP5TC2ZVPDCrHFzoiWF10RQjB7iYQpFztiFvtHeDTQhBgb1ZSWP9uoryxhwrtpOJ4Qwh0_T8Ij1r_rIhR-3QtyOltFkeL-pBOgcWhqcyjAMzqbzL5rpw3hzL_1GGsilx0uEvS-_Uo8gsbXJY4NwFysoU9pUazmXMq5nS3SflUsY4PENvhoAPQhCFwUoL55SYIVq72cnq2tnQsTk8YmIuf6BOjPBGvY7Q_5orZAtq0VmBx28MwS37dbf_mtD-ji7oUB5MVJu04A_OpOmjUtxBwm3h_ls_rKMgZ8MQYRUdOzOSP8Z75WIQnKrspkZEk1TT0td5BBwfONJsNkk-3QXsXPPLWvx1VuDJOyiYbKNCbQnl8o7_n5w","{\\"assistant_caller\\":\\"comet_above_composer\\",\\"conversation_guide_session_id\\":null,\\"conversation_guide_shown\\":null}"],"feedback_source":"PROFILE","idempotence_token":"client:%s","session_id":"49f6a778-b24f-4a62-b6aa-c1e8e311d2a1","actor_id":"%s","client_mutation_id":"3"},"inviteShortLinkKey":null,"renderLocation":null,"scale":1.5,"useDefaultActor":false,"UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute"}'%(feed_id, textComment, uuid.uuid1(), self.idFacebook), '7131632766860422')).json()
            if response['data']['comment_create']['feedback']['id'] == feed_id: return True, "Comment thành công"
        except Exception as e: print(e)
        return False, "Thất bại"

    def share(self, idPost: str):
        try:
            link = self.__client.get(f'https://facebook.com/{idPost}').url
            if 'groups' in link: typeShare = '37'
            else: typeShare = '22'
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":%s,\\"share_params\\":[%s]}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"idempotence_token":"%s","is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"CometGroupPermalinkRoot.react,comet.group.permalink,unexpected,1696419586408,407835,2361831622,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1696419575572,368790,190055527696468,229#230#340#301"},"source":"www","tracking":["AZXOeQspNNu5UOghII_ub19dAdDhJVhBVMZ7cXBmmVv34U6-9YuuvsjvU96CWpOlH9XBzZJMBUXZdQaI2483eRIy1KuZewx0a6lha7FdEI2x5NJTntSqjIeSmVN8MAJSquFxtaprOH7BfftEFOQWyz_K5JwhgR37AlcoiggdVfhizh2jih1vy5aCAB4pJHYTnJp9gUAaYz_cfRpczQHsaKDUJ8tZCmoOtPQ8VLWNHR_HWATDUfQWNd1yIdXKAiyQFuDtwY1dxaDWLeCy90zzowgDOcoGIZ-ZhGkTyUrj1-1PXvB5M6A720T2kP10HbtPUd0mQW26gxBTE76bMskxw5UkT9TC0rXY3I3IVRBbgrgVjMGcCXZDJ_aWHKm05iRUThUR-ex693qZyR5M1QzGhjxJij7rVDYMNIzv8AET_tCAFqofjs4Q3SnfGRBrvdAfZh_4qc8bkliPDK-I6cNZRo8fSWyM41y3ISMxcmZn3TzGiMcEAza0T8wERBe4wZBakd19myCLXvPg_YmRJHfWJD029_uMYwOiTb2mKJdKaojDornrReljiI_HDSp1U5XnlF9mR1CXAUANRtpXtOQF5WqYv62Dx0GpIShYdslxeViky8nvPj7S8Hizy-W7zaZWy72rtdRp5VN9H3SjEZ2IN6qEy2Xt67BtesmdeoZXKTyaQ8f2aIRVTil5yn8XKWVoJahPas4N9GN5epAMpohbJFRiiaEK4863AbcbdRN7a1zRIRKhxvKhB_hWNa1H1ejaHt_jMU0FaxwemnGyXN0QZX-TX4qtLaEkYsWjt52hhSuqs7puoJ3kwjfIRt5VO-PplCAvIeOHf7ly0b2PzEHyF8p4Cwvx3Hr_3JRBP-TE-OCRt0KosWSZTJBa-2EB3j5AeDNTAxkOBgIA3GDpni2WnXc4oML5qnOszBxfzCmoehK3o-PgiudFZCyo14wjYCjBVu8ndXbihcMqqJzkCDbxzCYhmDP2IaSVlAFeEsfDs1MPnQ"],"actor_id":"%s","client_mutation_id":"1"},"renderLocation":"homepage_stream","scale":1.5,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery","__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}'%(typeShare, idPost, uuid.uuid1(), self.idFacebook), '6694283607321722')).json()
            if response['data']['story_create']['story']['id']: return True, "Share thành công"
        except Exception as e: print(e)
        return False, "Thất bại"
    
    def likePage(self, idPage: str):
        try:
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"input":{"is_tracking_encrypted":true,"page_id":"'+idPage+'","source":"unknown","tracking":[],"actor_id":"'+self.idFacebook+'","client_mutation_id":"2"},"isAdminView":false}', '5556947024325929')).json()
            d = response['data']['page_like']['page']['is_viewer_fan']
            return d, "Thích trang" + str('thành công' if d == True else 'thất bại') 
        except:pass
        return False, "Thất bại"

    def ratePage(self, idPage: str, textRate: str):
        try:
            response=self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"input":{"composer_entry_point":"inline_composer","composer_source_surface":"page_recommendation_tab","source":"WWW","audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"message":{"ranges":[],"text":"'+textRate+'"},"with_tags_ids":[],"text_format_preset_id":"0","page_recommendation":{"page_id":"'+idPage+'","rec_type":"POSITIVE"},"actor_id":"'+self.idFacebook+'","client_mutation_id":"1"},"feedLocation":"PAGE_SURFACE_RECOMMENDATIONS","feedbackSource":0,"scale":1,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","UFI2CommentsProvider_commentsKey":"ProfileCometReviewsTabRoute","hashtag":null,"canUserManageOffers":false}', '5737011653023776')).json()
            try: response['data']['story_create']['story_id']; return True, "Đánh giá trang thành công"
            except: pass
        except:pass
        return False, "Thất bại"
    
    def joinGroup(self, idGroup: str):
        try:
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"feedType":"DISCUSSION","groupID":"'+idGroup+'","imageMediaType":"image/x-auto","input":{"group_id":"'+idGroup+'","source":"group_mall","actor_id":"'+self.idFacebook+'","client_mutation_id":"3"},"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall"}', '8097744130297884')).json()
            try: response['data']['group_request_to_join']['group']['id']; return True, "Tham gia nhóm thành công"
            except: pass
        except Exception as e:print(e)
        return False, "Thất bại"

    def switch_language(self):
        try:
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"locale":"vi_VN","referrer":"WWW_ACCOUNT_SETTINGS","fallback_locale":null}', '6451777188273168')).text
            return response['data']['updateLanguageLocale']['success']
        except Exception as e:pass

    def getPage(self):
        try:
            response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"scale":1}', '7111844212168519')).json()
            return response['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
        except: pass
    
    def get_data_post(self, idPost: str , type: str):
        feed_id = base64.b64encode("feedback:{}".format(idPost).encode('utf-8')).decode('utf-8')
        match type:
            case 'reaction':
                doc_id = 6099931570107234
            case 'share':
                doc_id = 9983524998356363
        
        response = self.__client.post('https://www.facebook.com/api/graphql/', data=self.__fectData('{"feedbackTargetID": "%s","scale":1}'%(feed_id), str(doc_id))).json()
        count = 0
        match type:
            case 'reaction':
                for data in response['data']['node']['top_reactions']['summary']:
                    try: count +=int(data['reaction_count'])
                    except: pass
        
            case 'share':
                count += response['data']['feedback']['reshares']['count']
        return count

    def view_live(self, live_id: str):
        try:
            data = {    
                'd': '{"pps":{"m":true,"pf":3368,"s":"playing","sa":2757389},"ps":{"m":true,"pf":13608,"s":"playing","sa":2757389},"si":"f15a9d1e26e924","so":"tahoe::topic_live","vi":"' + live_id + '","tk":"8Qv0Li7gMFJ5BBFyb1m6yBHLCpEUYQ1eOTCdZrxLR1Y1myQk+aSMWGOI+1BZoJCHIcDB2DEdv0JISR+KBV034w==","ls":true}',
                '__user': self.idFacebook,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'lsd': self.lsdFacebook,
            }
            response = self.__client.post('https://www.facebook.com/video/unified_cvc/', data).text
            if "LIVE" in response: return True, "View live thành công"
        except: pass
        return False, 'View live thất bại'
import threading
import time
idlive = input("Nhập Id Live: ")
def main(cookie, idlive):
    fb = FacebookMain()
    if fb.addCookie(cookie)[0] == True:
        print(fb.view_live(idlive))
        

while True:
    with open("Cookie.txt", 'r', encoding='utf-8') as f:
        cookie_lines = f.readlines()
        for cook in cookie_lines:
            cookie = cook.strip()
            threading.Thread(target=main, args=(cookie, idlive),).start()
    time.sleep(10)



