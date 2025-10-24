# Sicherheitsrichtlinien

## Webhook-Validierung
- Prüfe HMAC-Signatur jedes eingehenden OpenAI-Events.
- Verwerfe Events mit abgelaufener oder doppelter responseId.

## Secrets & Keys
- Keine Secrets im Repo.
- Alle Keys als ENV-Variablen.
- Rotation alle 90 Tage empfohlen.

## Authentifizierung
- GitHub App Tokens über hub4j erzeugen.
- Keine Personal Tokens im Code.
