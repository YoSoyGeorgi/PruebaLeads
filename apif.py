from apify_client import ApifyClient
import json

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_VzpK4MIwUlm2F8CrbaFxWDupkPtuOp09Zy3Y")

# Prepare the Actor input
run_input = {
    "cookie": [
        {
            "domain": ".linkedin.com",
            "expirationDate": 1720997479,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_gcl_au",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "1.1.2138974617.1708963552",
            "id": 1
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1717425396,
            "hostOnly": False,
            "httpOnly": False,
            "name": "_guid",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "3e12fe0f-b083-414b-9658-9e216fb444f6",
            "id": 2
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1715814302,
            "hostOnly": False,
            "httpOnly": False,
            "name": "aam_uuid",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "02995545190452601583378045147186296822",
            "id": 3
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1728773506,
            "hostOnly": False,
            "httpOnly": False,
            "name": "AMCV_14215E3D5995C57C0A495C55%40AdobeOrg",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "-637568504%7CMCIDTS%7C19829%7CMCMID%7C03532731022193911573327620356049962045%7CMCAAMLH-1713826306%7C7%7CMCAAMB-1713826306%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1713228706s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C956283887",
            "id": 4
        },
        {
            "domain": ".linkedin.com",
            "hostOnly": False,
            "httpOnly": False,
            "name": "AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": True,
            "storeId": "0",
            "value": "1",
            "id": 5
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1715745690,
            "hostOnly": False,
            "httpOnly": False,
            "name": "AnalyticsSyncHistory",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQJDaFoVRgnAywAAAY7f6n5psX3OAlrUxpgKQWdnNEApeM-Lxp33xPS9btNljDX45F5jfW5lbzVQsBt-7eDPQg",
            "id": 6
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1744758301.644889,
            "hostOnly": False,
            "httpOnly": False,
            "name": "bcookie",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "\"v=2&9bc77e8e-f01b-447d-867d-bb89df72d7e1\"",
            "id": 7
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1741185398,
            "hostOnly": False,
            "httpOnly": True,
            "name": "dfpfpt",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "79dab86d27774808a3bcc429575184db",
            "id": 8
        },
        {
            "domain": ".linkedin.com",
            "hostOnly": False,
            "httpOnly": True,
            "name": "fptctx2",
            "path": "/",
            "sameSite": "lax",
            "secure": True,
            "session": True,
            "storeId": "0",
            "value": "taBcrIH61PuCVH7eNCyH0B9zcK90d%252bIeoo1r5v7Zc27Y4HAOU4Dxi99n4Gn0Z6TBtT6S1uMmn0cMe8ON%252bBsqUKOz26s0z2cZZCGEiQyzNH08Xnc3DUB5W1%252bo6IcXQtFb8Dm8ogwCLvZj2hDeDxStpL%252ba4uWn%252b99BrFIi%252fqTU73dMs9ts8144%252fS1GUFJCLHBMp4t29SidMMkOKri4IEjodfr22tZlpZ5CNk4F7w5PNbu28oxESvNV3dSfIPx9THo4hN1s%252bIZEA2VfNPI9Wy%252fb%252bLThp4y6QzlfRwVEjMYRvdgl29jwARt4tpboWxXF35e2RnnEv57JTTxgFm7ZaguRKZcLvmAhBNB9JMVjuESkQ5c%253d",
            "id": 9
        },
        {
            "domain": ".linkedin.com",
            "hostOnly": False,
            "httpOnly": False,
            "name": "lang",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": True,
            "storeId": "0",
            "value": "v=2&lang=es-es",
            "id": 10
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1720998301.644803,
            "hostOnly": False,
            "httpOnly": False,
            "name": "li_sugr",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "c9dad632-61d9-41ea-8460-41c742ef08db",
            "id": 11
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1720997501.377101,
            "hostOnly": False,
            "httpOnly": False,
            "name": "liap",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "True",
            "id": 12
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1713240091.790574,
            "hostOnly": False,
            "httpOnly": False,
            "name": "lidc",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "\"b=TB46:s=T:r=T:a=T:p=T:g=145:u=52:x=1:i=1713222281:t=1713240071:v=2:sig=AQGTH6wpR7ru28qb-27sCKKSCicsypmn\"",
            "id": 13
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1715745691,
            "hostOnly": False,
            "httpOnly": False,
            "name": "lms_ads",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQF0Tf-Ct2P5yAAAAY7f6n-c__GDQpjPO6Z_yCoEVUXiml5VtaS1_WvoigfjoEieRb-Ez5T9aKiia8CV6Wf71dIFpAxjCdts",
            "id": 14
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1715745691,
            "hostOnly": False,
            "httpOnly": False,
            "name": "lms_analytics",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQF0Tf-Ct2P5yAAAAY7f6n-c__GDQpjPO6Z_yCoEVUXiml5VtaS1_WvoigfjoEieRb-Ez5T9aKiia8CV6Wf71dIFpAxjCdts",
            "id": 15
        },
        {
            "domain": ".linkedin.com",
            "hostOnly": False,
            "httpOnly": False,
            "name": "sdsc",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": True,
            "storeId": "0",
            "value": "22%3A1%2C1713220997359%7EJBSK%2C0QoC1BqIbaZ%2BfodDZIZIzBvsGg6A%3D",
            "id": 16
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1715814301,
            "hostOnly": False,
            "httpOnly": False,
            "name": "UserMatchHistory",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQLm_FGgJ1n31gAAAY7kAWV4D2Qk0LJm5ikHEmzcxR3w6rvNUIhUW9SQcc0YG361D7CuAiJB9Ri2_jcxbt7_u3cSp1nPFq5qjLSzB2JZgVi64NgzG3Mpw4CSivQc2pv7y-vM1InSd0wVVUNfcnN72beDcZad3cEoR0U0o0Jd7B-1rgqSlD71bm0LaFdvLfTat6E5s0szt7-OaPRkTfds-3sWlMAqn7agoB0_SWBI8rsEkq8oyFhmCM881u2gjItacbK4zWtorLTxytD_OjeO0EyL-xahVo5ghGhmAuv5UkPSyscsXTgZ2r9m3JxBqSgdvkT-G6Q",
            "id": 17
        },
        {
            "domain": ".linkedin.com",
            "expirationDate": 1747781482.319156,
            "hostOnly": False,
            "httpOnly": False,
            "name": "visit",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "v=1&M",
            "id": 18
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1744757501.546035,
            "hostOnly": False,
            "httpOnly": True,
            "name": "bscookie",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "\"v=1&202402261605469accc0f0-2f1a-4d0f-89fc-289dd1a365f9AQFixe-3uD7OSuKcLWx-EJD6gER9BO4q\"",
            "id": 19
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1720997501.37715,
            "hostOnly": False,
            "httpOnly": False,
            "name": "JSESSIONID",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "\"ajax:4368900647953205497\"",
            "id": 20
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1744757501.377039,
            "hostOnly": False,
            "httpOnly": True,
            "name": "li_at",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQEDAUo4yuoFRkiEAAABjuP1M2EAAAGPCAG3YU4Aa2BTpJCfRzFoM1ghEuP_GWJbDsqrgOzHCI8jWmikrkrBvjs-S8XFSMeVEuLsIj0MOwLl3YtTB6N4cusFhAIIYPWzx5oKdHZHtM4nf-UdwzxNy5ba",
            "id": 21
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1744757501.376633,
            "hostOnly": False,
            "httpOnly": True,
            "name": "li_rm",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQENUYx-QFKggQAAAY7j6xmJMoqJf8sMQ7wOmaPGqAbAhhNHdG_0dzPI6E9JmbABh5TaTG79DEX-WDe4FdbdyoT1MZVKwXoFYnrJyDcf6GzYfOKDhUiGIKskER3abJzjt9KQYP4FKVaDobbw_XayQ77PXrEYzh6zzaJaYQHBArw3pFsInseiaUxXUCKQdJ6zEdjSsaO4kcKlRNmI8waxYxiv5szEDB8N_bOIxRY6e2ufxVg6GmtfKyCH6U14iEG_dxU1reQ6L6Ja5Ubs9tagYsiZUQvTZbgLnWV7t4IlCyiTT4YMicbmxqDA31GKvrozP8CBslT2ACMP5PKBhSY",
            "id": 22
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1728774298,
            "hostOnly": False,
            "httpOnly": False,
            "name": "li_theme",
            "path": "/",
            "sameSite": "unspecified",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "light",
            "id": 23
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1728774298,
            "hostOnly": False,
            "httpOnly": False,
            "name": "li_theme_set",
            "path": "/",
            "sameSite": "unspecified",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "app",
            "id": 24
        },
        {
            "domain": ".www.linkedin.com",
            "expirationDate": 1714431898,
            "hostOnly": False,
            "httpOnly": False,
            "name": "timezone",
            "path": "/",
            "sameSite": "unspecified",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "America/Mexico_City",
            "id": 25
        },
        {
            "domain": "www.linkedin.com",
            "expirationDate": 1713826294.585376,
            "hostOnly": True,
            "httpOnly": False,
            "name": "fcookie",
            "path": "/",
            "sameSite": "no_restriction",
            "secure": True,
            "session": False,
            "storeId": "0",
            "value": "AQGiNyalfvTTBgAAAY7j9RkxXYecf55F3qeKIMyqLqY7DxIqN_nadf0hgcJ__7f2gIu--vNJNH2V5ajSbwlvR2Qg2ckeQCI9XU-lRYTQbF_dTY75K2C4WXlYjvUUjlqRiWzM1HiQR06M3aNli42tJ6fEy4MPTF4c5xieD0SI9EqEX_qVPBn2BMymzKjf7imrYdUyfxe4totKxobUzAaHS8CZLV8cVzscBrsBR-ivED1pZDLVfltT9nsqIDm6HT_lcETKAxq+BgQx0nFKmOedrsQ/XSRGFYcXuWXeYcceTn4RC6Op22UM1kTU+rIF3zon5eIAdaMbwn3JE9Vph/kxlg==",
            "id": 26
        },
        {
            "domain": "www.linkedin.com",
            "expirationDate": 1713825644.534578,
            "hostOnly": True,
            "httpOnly": False,
            "name": "fid",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "AQE6H5KDbX_IUgAAAY7j6y3MF8jSwgK4QNnzi8xb39FAU1-T7xPmQZgRtxHszPJ5VJA7haoeJYuGxA",
            "id": 27
        },
        {
            "domain": "www.linkedin.com",
            "expirationDate": 1725201391,
            "hostOnly": True,
            "httpOnly": False,
            "name": "g_state",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "{\"i_t\":1709735791232,\"i_l\":0}",
            "id": 28
        },
        {
            "domain": "www.linkedin.com",
            "expirationDate": 1713225082.31888,
            "hostOnly": True,
            "httpOnly": False,
            "name": "li_g_recent_logout",
            "path": "/",
            "sameSite": "unspecified",
            "secure": False,
            "session": False,
            "storeId": "0",
            "value": "v=1&True",
            "id": 29
        }
    ],
    "maxDelay": 60,
    "minDelay": 15,
    "scrapeCompany": False,
    "urls": [
        "https://www.linkedin.com/in/jorge-luis-olvera-olvera-7a203a2a9/"
    ]
}

# Run the Actor and wait for it to finish
run = client.actor("PEgClm7RgRD7YO94b").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    # Formatear el resultado como JSON
    formatted_result = json.dumps(item, indent=4)
    # Imprimir el resultado formateado
    # Obtener el nombre y la ocupación del perfil
    first_name = item.get("firstName", "")
    last_name = item.get("lastName", "")
    occupation = item.get("occupation", "")
    summary = item.get("summary", "")
    industry_name = item.get("industryName", "")
    company_name = item.get("companyName", "")

    # Imprimir el nombre y la ocupación
    print("Nombre:", first_name, last_name)
    print("Ocupación:", occupation)
    print("Descripción:", summary)
    print("Giro de la empresa:", industry_name)
    print("Nombre de la empresa:", company_name)

