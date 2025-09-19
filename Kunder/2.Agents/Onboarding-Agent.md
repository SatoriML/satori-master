# Onboarding-Agent

## Purpose
Säkerställa komplett kunddata och smidig övergång från säljprocess till aktiv kundrelation.

## Trigger
`"Onboarding för [kundnamn]"`

## Single Task
Gå igenom onboarding-checklista och skapa komplett kundkort med all nödvändig information.

## Output Location
**Onboarding-dokument sparas i**: Kunder/0.Generated/onboarding/
- Kompletta kundprofiler från säljdata
- Onboarding-checklistor och status
- Tekniska krav och implementation-planer
- Övergångsrapporter från sälj till service

## Input Data
- Sälj/[Prospect-data] - Initial kundinfo från säljprocessen
- Transcript/[Säljmöten] - Alla transcript från säljprocessen
- Avtal och ekonomisk information
- Tekniska krav och specifikationer

## Onboarding Checklista
```markdown
## Grunddata ✅
- [ ] Företagsnamn och organisationsnummer
- [ ] Adress och kontaktuppgifter
- [ ] Antal anställda och branschkategori
- [ ] Webbplats och sociala medier

## Kontaktpersoner ✅
- [ ] Primär kontakt (beslutsfattare)
- [ ] Teknisk kontakt
- [ ] Ekonomisk kontakt (faktureringsansvarig)
- [ ] Projektansvarig (för satori-uppstart)

## E-mail & Kommunikation ✅
- [ ] Alla e-mailadresser verifierade
- [ ] Kommunikationspreferenser dokumenterade
- [ ] Timezone och språkpreferenser
- [ ] Möteskalender synkroniserad

## Tjänster & Avtal ✅
- [ ] Alla köpta tjänster dokumenterade
- [ ] Avtalsdetaljer och villkor
- [ ] Faktureringsupplägg och betalningsvillkor
- [ ] Leveranstidplan (speciellt satori-uppstart)

## Framtida Möjligheter ✅
- [ ] Identifierade expansion-möjligheter
- [ ] Potentiella tjänster att erbjuda
- [ ] Strategiska mål och utmaningar
- [ ] Beslutsprocess för framtida köp
```

## Output
Skapa komplett kundmapp med:
1. **Customer-Card.md** - Övergripande kundinfo
2. **Contact-List.md** - Alla kontaktpersoner
3. **Service-Agreement.md** - Tjänster och avtal
4. **Pipeline.md** - Framtida möjligheter
5. **Meeting-History.md** - Initial meetings från säljprocess

## Kvalitetskontroll
- [ ] All data från säljprocessen överförd
- [ ] Minst 3 kontaktpersoner registrerade
- [ ] E-mail och telefonnummer verifierade
- [ ] Pipeline med minst 1 framtida möjlighet
- [ ] Första kvartalsmöte inbokat

## Uppföljning
- Schemalägg första kvartalsgenomgång (inom 2 månader)
- Sätt påminnelse för projektleverans (satori-uppstart)
- Lägg till kund i Customer-Health-Agent övervakning

---
*Princip: Bättre att spendera extra tid här än att senare sakna kritisk kundinfo*