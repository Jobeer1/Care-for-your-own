# Sorg vir Jou Eie - Persoonlike Assistent

Hierdie persoonlike assistent-toepassing help jou met daaglikse take, skedulering en toegang tot inligting deur natuurlike taal te gebruik. Dit verstaan jou versoeke en bied persoonlike antwoorde.

## Aan die gang

Hier is hoe om die "Sorg vir Jou Eie" persoonlike assistent af te laai en te gebruik:

1.  **Gaan na die korrekte tak:**

    *   Wanneer jy die GitHub-bewaarplek besoek ([https://github.com/Jobeer1/Care-for-your-own](https://github.com/Jobeer1/Care-for-your-own)), kan jy op die `main` tak beland. Vir aflaaie het jy die `master` tak nodig.

    *   Klik op die tak-aftreklys (dit sê gewoonlik "main" of "master") en kies die `master` tak.

2.  **Laai die toepassing af:**

    *   **Maklikste manier (indien beskikbaar):** Gaan na die "Releases" bladsy op GitHub ([https://github.com/Jobeer1/Care-for-your-own/releases](https://github.com/Jobeer1/Care-for-your-own/releases)). As daar 'n voorafgeboude weergawe (soos 'n `.exe`-lêer) vir die `master` tak is, laai dit af. Dit is die eenvoudigste opsie.

    *   **Indien geen voorafgeboude weergawe:** As daar geen vrystellings is nie of jy die nuutste kode benodig, klik op die groen "Code" knoppie op die hoofbewaarplekbladsy (maak seker jy is op die `master` tak). Klik dan "Download ZIP".

3.  **Installeer (as jy die kode afgelaai het):**

    *   As jy 'n voorafgeboude weergawe afgelaai het, kan jy hierdie stap oorslaan.

    *   As jy die kode as 'n ZIP-lêer afgelaai het, pak die ZIP-lêer uit na 'n gids op jou rekenaar.

    *   **Belangrik:** Hierdie toepassing benodig Python. As jy nie Python het nie, laai dit af vanaf [https://www.python.org/downloads/](https://www.python.org/downloads/). Installeer Python.

    *   Maak die gids oop waar jy die kode uitgepak het.

    *   Maak 'n "Command Prompt" (op Windows) of "Terminal" (op Mac/Linux) oop.

    *   In die opdragprompt of terminaal, navigeer na die gids waar jy die kode uitgepak het. Jy kan dit doen deur `cd` te tik, gevolg deur die pad na die gids. Byvoorbeeld: `cd C:\Users\JouNaam\Downloads\Care-for-your-own`.

    *   Tik `pip install -r requirements.txt` en druk Enter. Dit sal al die nodige komponente installeer. As jy nie 'n `requirements.txt`-lêer het nie, tik die volgende in plaas daarvan: `pip install flask azure-cognitiveservices-speech google-generativeai python-dotenv`

4.  **Kry API-sleutels (Belangrik!):**

    Hierdie toepassing gebruik API-sleutels om te werk. Jy sal jou eie sleutels van die volgende dienste moet kry:

    *   **Gemini API-sleutel:** Jy sal moet aanmeld vir 'n Google Cloud-rekening en die Gemini API aktiveer. Jy kan instruksies oor hoe om dit te doen in die Gemini-dokumentasie vind.

    *   **Azure Cognitive Services API-sleutels:** Jy sal 'n Azure-rekening moet skep en inteken op die Azure Cognitive Services for Speech. Jy kan instruksies oor hoe om dit te doen in die Azure-dokumentasie vind.

5.  **Konfigurasie (Stel die sleutels op):**

    *   Vind die lêer met die naam `config.ini.example` in die toepassingsgids.

    *   Maak 'n kopie van hierdie lêer en hernoem die kopie na `config.ini`. (Regskliek op die lêer, kies "Copy", regskliek dan in dieselfde gids en kies "Paste". Regskliek dan op die nuwe lêer en kies "Rename".)

    *   Maak die `config.ini`-lêer in 'n teksredigeerder (soos Notepad) oop.

    *   Binne die `config.ini`-lêer sal jy plekke sien om jou API-sleutels in te voer. Plak die Gemini API-sleutel waar dit sê `GEMINI_API_KEY =`, en die Azure-sleutels waar dit sê `AZURE_SUBSCRIPTION_KEY =` en `AZURE_REGION =`.

    *   Stoor die `config.ini`-lêer.

6.  **Begin die toepassing:**

    *   **As jy 'n voorafgeboude weergawe afgelaai het:** Dubbelklik die `.exe`-lêer om die toepassing te begin.

    *   **As jy die kode afgelaai het:** Maak die opdragprompt of terminaal oop, gaan na die toepassingsgids en tik `python app.py` en druk Enter.

7.  **Gebruik die toepassing:**

    Beskryf hoe om jou toepassing te gebruik. Byvoorbeeld:

    *   "Tik jou versoeke in die opdragprompt of terminaal."
    *   "Die toepassing sal met teks en/of spraak reageer."

## Probleemoplossing

As jy enige probleme het, kyk asseblief na die volgende:

*   Maak seker dat jy al die nodige komponente geïnstalleer het.
*   Maak seker dat jy die API-sleutels korrek in die `config.ini`-lêer ingevoer het.
*   Kyk na die toepassing se uitset in die opdragprompt of terminaal vir enige foutboodskappe.

As jy steeds probleme het, kan jy 'n "Issue" op GitHub skep (gaan na die "Issues"-oortjie op die bewaarplekbladsy) om hulp te vra.

## Kontak
ysterjobeer@gmail.com 
