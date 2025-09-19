# Document-Flow & Architecture

## Primär Dokumentstruktur

### Kunder/ - Huvudkälla för Dokumentation
Alla kundrelaterade dokument centraliseras här för enkel åtkomst och kontinuitet.

```
Kunder/[KundNamn]/
├── 1.Möten/
│   ├── Meeting-protocols/
│   ├── Transcripts/
│   └── Action-items/
├── 2.Timmar-fakturering/
│   ├── Time-tracking/
│   ├── Invoices/
│   └── Financial-records/
├── 3.Tjänster/
│   ├── Project-documentation/
│   ├── Deliverables/
│   └── Technical-specs/
├── 4.Strategi/
│   ├── Contracts/
│   ├── Strategic-decisions/
│   └── Roadmaps/
└── 5.Notes-Todos/
    ├── Ongoing-communication/
    ├── Quick-notes/
    └── Todo-lists/
```

### Transcript/ - Centraliserad Mötesarkiv
Alla transkriberade möten samlas här för analys och referens.

```
Transcript/
├── Internal-meetings/
│   ├── Team-meetings/
│   └── Strategy-sessions/
├── Customer-meetings/
│   ├── [KundNamn]/
│   └── [Date-based organization]/
└── Sales-meetings/
    ├── New-prospects/
    └── Follow-ups/
```

## Dokumentflöden

### 1. Meeting → Documentation Flow
```
Meeting (Live)
    ↓ [Transkription]
Transcript/ (Raw audio → text)
    ↓ [Processing]
Protokoll (Structured summary)
    ↓ [Arkivering]
Kunder/[Namn]/1.Möten/ (Final storage)
    ↓ [Action Extraction]
Kunder/[Namn]/5.Notes-Todos/ (Follow-up items)
```

### 2. Decision → Documentation Flow
```
Decision (Meeting/Discussion)
    ↓ [Documentation]
Decision Document (Structured)
    ↓ [Kategorisering]
IF strategiskt → Kunder/[Namn]/4.Strategi/
IF operativt → Kunder/[Namn]/3.Tjänster/
IF administrativt → Kunder/[Namn]/5.Notes-Todos/
    ↓ [Version Control]
Version 1.0 (Live document)
    ↓ [Updates]
Version 1.1, 1.2... (Iterationer)
```

### 3. Communication → Archive Flow
```
Communication (Email/Teams/SMS)
    ↓ [Relevans Bedömning]
IF kundrelaterat → Continue
IF internt only → Local archive
    ↓ [Customer Mapping]
Identifiera rätt kund
    ↓ [Kategorisering]
IF avtal → 4.Strategi/
IF projekt → 3.Tjänster/  
IF rutinmässigt → 5.Notes-Todos/
    ↓ [Arkivering]
Structured storage med metadata
```

## Versionshantering System

### Version Numbering Logic
- **0.1 - 0.9**: Draft/utvecklingsfaser
- **1.0**: Första "live" eller färdiga versionen
- **1.1 - 1.9**: Mindre uppdateringar av live dokument
- **2.0**: Major revision eller omfattande uppdatering

### Version Control Process
1. **Check Existing**: Kontrollera nuvarande version
2. **Determine Change Level**: Minor vs major update
3. **Assign Number**: Enligt numbering logic
4. **Document Changes**: Versionsloglgg obligatorisk
5. **Archive Previous**: Behåll historical versions
6. **Update References**: Korsreferenser till nya versionen

## Metadata Standards

### Obligatorisk Metadata
```markdown
---
Titel: [Dokumentnamn]
Version: [Versionsnummer]
Skapad: [YYYY-MM-DD] (Aktuellt datum: 2025-09-04)
Uppdaterad: [YYYY-MM-DD]
Författare: [Person]
Kund: [Om relevant]
Status: [Draft/Review/Final/Archive]
Relaterade dokument: [Links]
Nyckelord: [Tags för sökbarhet]
---
```

### Datum Hantering
- **Kritiskt**: Använd alltid live/aktuellt datum (2025-09-04)
- **Aldrig**: Model default dates
- **Format**: YYYY-MM-DD (ISO standard)
- **Timezone**: Svensk tid (CET/CEST)

## Quality Gates

### Innan Arkivering
- [ ] Korrekt datum (2025-09-04, inte model default)
- [ ] Rätt versionsnummer enligt sekvens
- [ ] Complete metadata fylld i
- [ ] Relevant kund identificerad
- [ ] Rätt mappstruktur destination
- [ ] Korsreferenser uppdaterade

### Sökbarhet Requirements
- [ ] Beskrivande filnamn
- [ ] Nyckelord/tags completeness
- [ ] Structural consistency
- [ ] Cross-referencing accuracy

## Integration Points

### Document-Manager-Agent Responsibilities
- Automated categorization
- Version number assignment
- Metadata validation
- Quality gate enforcement
- Cross-reference maintenance

### Search & Retrieval
- Filename standardization
- Tag-based indexing
- Date-range queries
- Customer-specific searches
- Project/service filtering

## Backup & Redundancy
- **Primary**: Live document structure
- **Secondary**: Version archives  
- **Tertiary**: Cross-references preservation
- **Recovery**: Document relationship rebuilding

---
*Dokumenterad av: CEO Joachim Sahlin*  
*Uppdaterad: 2025-09-04*