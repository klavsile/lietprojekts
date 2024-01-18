# Lietojumprogrammatūras automatizēšanas rīki projekts
Klāvs Īle: 231RDB027

## Projekta uzdevums

```
Noslēguma projekts ir jūsu iespēja izmantot jauniegūtās prasmes, lai izstrādātu pilnvērtīgo programmatūru noteikto uzdevuma risināšanai. Projektā jāizmanto zināšanas, kas ir iegūtas kursa laikā, bet projekta uzdevumu jāģenerē jums pašiem. Mēs gribam, lai Jūs izveidotu sistēmu, kas automatizēs kādu no jūsu ikdienas uzdevumiem.

Tā kā programmatūras izstrāde reti kad ir vienas personas darbs, jums tiek dota iespēja sadarboties ar vienu vai diviem kursabiedriem šī gala projekta izstrādes laikā. Protams, tiek sagaidīts, ka katrs students jebkurā šādā grupā vienlīdzīgi piedalās grupas projekta izstrādē. Turklāt tiek sagaidīts, ka divu vai trīs personu grupas projekta apjoms attiecīgi būs divreiz vai trīsreiz lielāks nekā vienas personas projekts.

Uzdevuma skaidrojums

Projekta izstrādes laikā Jums jāizmanto GitHub, kur Jūs publicēsiet ne tikai programmas kodu, bet nepieciešamo programmatūras dokumentāciju. 

Izstrādājot projektu Jums ir nepieciešams izveidot README.md datni, kur Jūs (OBLIGĀTI latviešu valodā):

·       detalizēti aprakstīsiet projekta uzdevumu;

·       izskaidrosiet kādas Python bibliotēkas un kāpēc tiek izmantotas projekta izstrādes laikā

·       aprakstīsies programmatūras izmantošanas metodes

Var pievienot video (saiti uz to), kurā būs parādīts jūsu programmatūras darbībā un rezultāts.

Ja jums nav pieredzes ar Markdown sintaksi, jums varētu būt noderīga GitHub pamatinformācija parrakstīšana un formatēšana.

Standarta programmatūras projekta README faili bieži var sasniegt tūkstošus vai pat desmitiem tūkstošu vārdu. Jūsu failam nav jābūt tik lielam, bet tur ir jābūt vismaz vairākiem simtiem vārdu, kas detalizēti apraksta projektu!

Visas projekta izstrādes izmaiņas tiek uzglabātas GitHub krātuvē, kas ļauj izsekot projekta izstrādes gaitu.
```

### Projekta apraksts
Programma, kas pārveido dotos failus uz citiem faila formātiem: .gif, .mp4, .mov.
Jābūt iespējai iestatīt izejas faila rezolūciju.
Programmai jābūt saprotamai lietotāja saskarnei un faila izvēles logam.

## Python bibliotēkas


```python
import os
```
os bibliotēka tiek izmantota, lai strādātu ar direktorijām.

```python
import tkinter as tk
from tkinter import font
from tkinter import filedialog as fd
```
tkinter bibliotēka tiek izmantota, lai veidotu lietotāja saskarni un atvērtu faila izvēles logu.

```python
import ffmpeg
```
ffmpeg bibliotēka tiek izmantota, lai pārveidotu failus uz citiem formātiem.

```python
from datetime import datetime
```
datetime bibliotēka tiek izmantota, lai noteiktu sistēmas laiku, priekš failu nosaukumu veidošanas.

## Programmas izmantošana
#### ❗❗❗ LAI IZMANTOTU SISTĒMĀ IR VAJADZĪGS UZSTĀDĪT FFMPEG UN LIETOTĀS BIBLIOTĒKAS ❗❗❗
ffmpeg vajag pievienot PATH vai ielikt folderī, kurā atrodas python.exe (it īpaši, ja PATH nestrādā) [Info par šo problēmu](https://stackoverflow.com/a/72549351)

1. Palaist programmu main.py
2. Ierakstīt Width un Height logos vēlēto rezolūciju (nav obligāti, ja atsās laukus tukšus, tad rezolūcija paliks tāda pati, kā ievades failam)
3. Nospiest pogu vēlamajam izvades formātam
4. Izvēlēties ievades failu
5. Gaidīt, kamēr izvades fails tiek izveidots

## Video piemērs
> https://streamable.com/9lyrkw
