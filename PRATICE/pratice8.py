#The "Log Sifter" (Lambdas + Filter)

logs  = [{"event": "login", "level": "INFO"}, {"event": "file_change", "level": "CRITICAL"}, {"event": "port_scan", "level": "CRITICAL"}]
critical_alerts = list(filter(lambda x:x["level"] == "CRITICAL",logs))
print(critical_alerts)


