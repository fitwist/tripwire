import gspread
import pandas as pd
import numpy as np
import plotly.express as px
import os

credentials = {
    "type": "service_account",
    "project_id": "dialogflow-293713",
    "private_key_id": "c5bde7cf8d3198ef6dbb13678f27a44dfa38fe1c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeT03JC7+LJEk8\n9CfaX+a5cQUoXqAxYehVgA8Ch7t7e22jEkg3dZdepWWwR2dYW5kSwhkK3V0YcxOO\nwkSGvEeqUI7zBX/gxXxuLDBD2xwCTI0moKE2g5a/lBzdbKhIcyle7V6Xdpz/mDsu\n8v2xffibkSwhQiQjvjkGnY8wfwnkQdJuqMDiuSm/h5dbckQ+GPsR+BZXDhqu+MW2\npt4IwItbshjkmyzm5ddwdnYl8a3NqenWrQgR++KJkySsyzQ3bCk5K2EHE7kEcpiD\naUEcgH+K7dg4+JNiaes8onlGe18GIA0vhh5L9Bdt4EwgWwVoHzhmJJH7XwKi8Nk5\njLPl6mq9AgMBAAECggEAJN0RHyVv8SneLwYoqJJn0ttFSPD96vniRNSYyi1KpDap\n4UzuyZFFkfnAO+PopfvQYXyWob/Jv5l+XqIQnHJH2to+60qmzDOYZbw+8fIZ69Qh\nEzNYzu2l4w8NiKcWaaZ9ZfgurGTnqqHreCOHnTbY9vq/VLBG45bWRxrV3sRaTI8E\new+NSXrdhu1yWEl9oByIMeJanDuGz69TV74ysIrtqMh6BPOK4zuty6g1V33J6Yqb\nO0DUnF31ht8hc2nLF1JndTEZ2tyQWR5IRGkM5hwsmn24zByhQmRnUqpshhtD2Dhk\ncGZkiTzSVmGy3YrVml5VcZ9PY6s6xi+nxw0zMWKiyQKBgQDLiYMKRb+VmpAuFg1D\nSaOKqadBuSIr//GjrGB9cg3eoZmqtEVCvTTLPVMZPgay2HOJVKSrsxhoSX/c1s04\np84QVesGtiEieb6BJmrn4zE0X+P9IJo3OBoLlW0PI1/lnEW9YRLEvxVdTSe80TkS\nVpBKP3B1mOB4aybQ/Gz+ekP6xQKBgQDHHXGhpNGjHHl57L7MQ0LaWyE13mxyAxkU\n8jB+0DNskkTniEx9ZJeHMn8Vs2n5K4NR0c0dFEjWozi/GgYCa4nnW5PxMAHHTtxH\nIIOd8+oOhxcjCJwRub+lfiw26OfVQ/zMcLOod2ND+1qYJ2bXm816r1t5t6Nog5jM\nSRFt0rgPmQKBgDT9OfZkrjoeoUa+SvmnpEInZPoBXtohqiE4cW53URES9VSx1g5I\nAAShlI7PzSKmo32vYaep2sLbz8QI0Cjd1xH9rFB0/i9hjq1E+TQhu9+sz0hJQpz5\nqB436sq0JPU8OBPTv/Uk4kUGH0BTIA6cJriNx5N2F4qCKvrhnOaroiMZAoGAFgoG\nR9QMeDdworQ3sjhHsA+iL2o9Kql5Hz5na8HzzzKpec82WDLIKujF9Er1keTlFitY\nvr0+CrPqVgy1WZM5omgaifm8WKk77IuGxfb3k0AUqYYMcFHVCqZakoFZF9v8oUxg\nNmdwj1fFAU5rLbZLGidKwsA20BywzvvPeA543RECgYEAyvL3S1ZZAGw4SXmXib3y\nXMeBC7SkMynyzaefsRgHb+jwfbJM0dkAXiaudLRlqQhW/cW2KF01Md4VLn/8/s6Q\nzE3zt+8ykMUnjKQInux7jcwr33AfJDYIFbMFFXHrDpeDuYUoseHZ4YBlIjO6NNDJ\nrftF5lLJ/mfKMesg8ULDVHI=\n-----END PRIVATE KEY-----\n",
    "client_email": "986281389469-compute@developer.gserviceaccount.com",
    "client_id": "107524889568738648427",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/986281389469-compute%40developer.gserviceaccount.com"
}

# Подгрузим таблицу с опрошенными
gc = gspread.service_account_from_dict(credentials)
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WFK-T5s2U1pSnfeaTx3VkRzt6-WEuQ2k8MY2TKkzNBc').sheet1
data = sheet.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

def create_chart(result_lst):
  # Преобразуем элементы списка в целочисленные
  lst = result_lst[1:]
  score = [eval(i) for i in lst]

  col = [score[0] * 3, score[2] * 3, score[4] * 3, score[6] * 3, score[8] * 3, score[10] * 3, 
        score[1] * 2 + score[12], score[3] * 2 + score[13], score[5] * 2 + score[14], score[7] * 2 + score[15], score[9] * 2 + score[16], score[11] * 2 + score[17]]

  # Превратим список очков в датафрейм, чтобы корректно отобразить паутинку
  df = pd.DataFrame({'category': ['Команда', 'Заинт. стороны', 'Подход и поставка', 'Планирование', 'Работа и измерение', 'Риски', 
                                  'Команда', 'Заинт. стороны', 'Подход и поставка', 'Планирование', 'Работа и измерение', 'Риски'],
                      'strength': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]})

  df['score'] = col

  # Присвоим значениям интервалов категории
  conditions = [
      (df['score'] == 0),
      (df['score'] >= 1) & (df['score'] <= 6),
      (df['score'] >= 7) & (df['score'] <= 12),
      (df['score'] >= 13) & (df['score'] <= 20)
  ]

  # Перечислим категории
  tiers = ['Новичок', 'Падаван', 'Рыцарь-Джедай', 'Мастер-Джедай']

  df['mark'] = np.select(conditions, tiers)
  df2 = df.assign(mark=pd.Categorical(df["mark"], ordered=False, categories=tiers))

  fig = px.line_polar(df2, r="score", theta="category", color="strength", line_close=True,
                      color_discrete_sequence=['#3b5998', '#52a9f9'], template="plotly_dark",
                      title=f"{result_lst[0]}, очков: {sum(col[:11])}")

  # Добавим заливку
  fig.update_traces(fill='toself')

  # Добавим подписи на шкале
  fig.update_layout(polar={"radialaxis":{"tickmode":"array","tickvals":[0, 7, 12, 20],"ticktext":tiers}})

  # Настроим легенду
  fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.01
  ))

  # Настроим кастомную легенду
  fig.data[0].name="Умения"
  fig.data[1].name="Проблемы"


  fig.write_image(f"{os.environ['SYSTEM_PATH']}{result_lst[0]}.jpeg")
  return

def interprete_score(result_lst):
    # Преобразуем элементы списка в целочисленные
    lst = result_lst[1:]
    score = [eval(i) for i in lst]

    scores = [score[0] * 3, score[2] * 3, score[4] * 3, score[6] * 3, score[8] * 3, score[10] * 3, 
          score[1] * 2 + score[12], score[3] * 2 + score[13], score[5] * 2 + score[14], score[7] * 2 + score[15], score[9] * 2 + score[16], score[11] * 2 + score[17]]
    
    skills_lst = scores[:5]

    # Определим минимальное умение
    skills_min = min(skills_lst)

    # Определим среднее значение по умениям
    def find_mean(lst):
        return sum(lst) / len(lst)
 
    skills_mean = find_mean(skills_lst)
    mean_min_diff = skills_mean - skills_min

    interpretation = []
    if mean_min_diff < 5:
      interpretation.append('У вас ровные компетенции\.')
    elif 5 <= mean_min_diff <= 10:
      interpretation.append('Из графика явно видно, что ваши компетенции развиты в разной степени\.')
    else:
      interpretation.append('Из графика явно видно, что ваши компетенции в разных сферах существенно различаются\. Постарайтесь обращать больше внимания на те сферы, которые у вас выпадают \– без этого не получится стать профессиональным РП\.')

    team_diff = scores[0] - scores[1] 
    stakeholders_diff = scores[2] - scores[3] 
    approach_diff = scores[4] - scores[5] 
    planning_diff = scores[6] - scores[7] 
    work_diff = scores[8] - scores[9] 
    risk_diff = scores[10] - scores[11] 
    
    if (team_diff > 0 and stakeholders_diff > 0 and approach_diff > 0 and planning_diff > 0 and work_diff > 0 and risk_diff > 0):
      interpretation.append('Хорошие новости – судя по всему в вашей текущей рабочей деятельности ваших компетенций хватает, чтобы справляться с возникающими проблемами\. Однако мы советуем не расслабляться – кто знает, какие вызовы ждут вас в будущем?.. ')
    else:
      # print(team_diff)
      # print(stakeholders_diff)
      # print(approach_diff)
      # print(planning_diff)
      # print(work_diff)
      # print(risk_diff)
      interpretation.append('Но обратите внимание: их часто недостаточно для того, чтобы решить возникающие проблемы в следующих сферах:')

    if team_diff > 0:
      interpretation.append('\n\- Команда')
    if stakeholders_diff > 0:
      interpretation.append('\n\- Заинтересованные стороны')
    if approach_diff > 0:
      interpretation.append('\n\- Подход и поставка')
    if planning_diff > 0:
      interpretation.append('\n\- Планирование')
    if work_diff > 0:
      interpretation.append('\n\- Работа и измерение')
    if risk_diff > 0:
      interpretation.append('\n\- Риски')
    else:
      pass
      
    output = ' '.join(interpretation)
    return output


def append_result(result_lst):
  body = result_lst
  sheet.append_row(body) 