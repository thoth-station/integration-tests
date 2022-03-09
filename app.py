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

"""Run integration tests and send e-mail report or save in an artifact directory."""

from behave.__main__ import main as behave_main
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import smtplib
import sys
import shutil

__version__ = "0.10.1"

_BEHAVE_REPORT_FILE = "behave-report.html"
_DEPLOYMENT_NAME = os.getenv("THOTH_DEPLOYMENT_NAME", "N/A")
_EMAIL_SMTP_SERVER = os.getenv("THOTH_EMAIL_SMTP_SERVER", "smtp.corp.redhat.com")
_EMAIL_TO = os.getenv("THOTH_EMAIL_TO", "aicoe-thoth-devops@redhat.com")
_EMAIL_FROM = os.getenv("THOTH_EMAIL_FROM", "noreply@redhat.com")
_GENERATE_REPORT = bool(int(os.getenv("GENERATE_REPORT", 0)))
_MAIL_REPORT = bool(int(os.getenv("MAIL_REPORT", 0)))
_TAGS = os.getenv("THOTH_INTEGRATION_TESTS_TAGS")
_BEHAVE_HTML_REPORT = "behave-report.html"
_ARTIFACTS_DIRECTORY = os.getenv("ARTIFACTS", None)


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
    return f"Integration tests update for {_DEPLOYMENT_NAME} ({today.strftime('%Y-%m-%d')} version {__version__})"


def send_email() -> None:
    """Send e-mail with begave test reports."""
    msg = MIMEMultipart()
    with open(_BEHAVE_REPORT_FILE, "r") as fp:
        report = fp.read()

    msg["Subject"] = _create_email_subject()
    msg["From"] = _EMAIL_FROM
    msg["To"] = _EMAIL_TO
    msg.attach(MIMEText(report, "html"))  # Message body.

    attachment = MIMEApplication(report, _subtype="html")
    attachment.add_header("content-disposition", "attachment", filename=_BEHAVE_REPORT_FILE)
    msg.attach(attachment)

    s = smtplib.SMTP(_EMAIL_SMTP_SERVER)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())
    s.quit()


def main() -> None:
    """Run main entry-point for s2i based integration tests."""
    args = ["--show-timings"]
    if _GENERATE_REPORT:
        args.extend(["-f", "html", "-o", "behave-report.html"])

    if _TAGS:
        args.extend(["--tags", _TAGS])

    # Pass any additional arguments to behave.
    args.extend(sys.argv[1:])

    _print_info()
    print("Tests are executed using", args, file=sys.stderr)

    try:
        exit_code = behave_main(args)
    except OSError:
        pass

    if _GENERATE_REPORT and _MAIL_REPORT:
        send_email()

    if _ARTIFACTS_DIRECTORY is not None:
        shutil.copy(_BEHAVE_HTML_REPORT, _ARTIFACTS_DIRECTORY)

    sys.exit(exit_code)


__name__ == "__main__" and main()
