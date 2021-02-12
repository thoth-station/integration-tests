#!/usr/bin/env python3
# Thoth's integration tests
# Copyright(C) 2021 Red Hat, Inc.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/

"""Send e-mail report, used to send reports to our mailing list."""

from behave.__main__ import main as behave_main
from datetime import date
from email.mime.text import MIMEText
import os
import smtplib
import sys

_BEHAVE_REPORT_FILE = "behave-report.html"
_DEPLOYMENT_NAME = os.getenv("THOTH_DEPLOYMENT_NAME", "N/A")
_EMAIL_SMTP_SERVER = os.getenv("THOTH_EMAIL_SMTP_SERVER", "smtp.corp.redhat.com")
_EMAIL_TO = os.getenv("THOTH_EMAIL_TO", "fpokorny@redhat.com")
_EMAIL_FROM = os.getenv("THOTH_EMAIL_FROM", "noreply@redhat.com")
_MAIL_REPORT = bool(int(os.getenv("MAIL_REPORT", 0)))
_BEHAVE_HTML_REPORT = "behave-report.html"


def _print_info() -> None:
    """Print test information."""
    print(
        f"""--------------------------------------------------------------------------------
> Tests are executed against {_DEPLOYMENT_NAME} deployment
> Tests are executed against User API at {os.getenv('THOTH_USER_API_HOST')}
> Tests are executed against Management API at {os.getenv('THOTH_MANAGEMENT_API_HOST')}
> Tests are executed against Amun API at {os.getenv('THOTH_AMUN_API_HOST')}
--------------------------------------------------------------------------------"""
    )


def _create_email_subject() -> str:
    """Create e-mail subject."""
    today = date.today()
    return f"Integration tests update for {_DEPLOYMENT_NAME} ({today.strftime('%Y-%m-%d')})"


def send_email() -> None:
    """Send e-mail with begave test reports."""
    with open(_BEHAVE_REPORT_FILE, "r") as fp:
        msg = MIMEText(fp.read(), "html")

    msg["Subject"] = _create_email_subject()
    msg["From"] = _EMAIL_FROM
    msg["To"] = _EMAIL_TO

    s = smtplib.SMTP(_EMAIL_SMTP_SERVER)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())
    s.quit()


def main() -> None:
    """Run main entry-point for s2i based integration tests."""
    args = ["--show-timings"]
    if _MAIL_REPORT:
        args.extend(["-f", "html", "-o", "behave-report.html"])

    # Pass any additional arguments to behave.
    args.extend(sys.argv[1:])

    _print_info()

    behave_main(args)

    if _MAIL_REPORT:
        send_email()


__name__ == "__main__" and main()
