import os

# Knowledge base documents content
DOCUMENTS = {
    "hr/employee_handbook.txt": """Employee Handbook

Welcome to Our Company
This handbook provides essential information about our company culture, policies, and expectations. We are a modern tech company committed to innovation, collaboration, and employee growth.

Our mission is to build products that make a difference. We value transparency, continuous learning, and work-life balance. This handbook will guide you through your journey with us.

Working Hours and Flexibility
We operate on a flexible schedule with core hours from 10 AM to 4 PM in your local timezone. You're expected to be available during core hours for meetings and collaboration.

Outside core hours, you have flexibility to manage your schedule. We trust you to deliver results and manage your time effectively. Remote work is fully supported.

Communication Expectations
We use Slack for daily communication, email for formal correspondence, and Zoom for video meetings. Response time expectations: Slack within 2 hours during work hours, email within 24 hours.

Always update your status when away from keyboard. Use Do Not Disturb mode outside working hours. Respect colleagues' time zones when scheduling meetings.

Professional Development
We invest in your growth through annual learning budgets, conference attendance, and internal training programs. Each employee receives $2000 annually for professional development.

You can use this budget for courses, certifications, books, or conference tickets. Submit requests through the HR portal with justification and expected outcomes.
""",

    "hr/leave_policy.txt": """Leave and Time Off Policy

Annual Leave Entitlement
All full-time employees receive 20 days of paid annual leave per year, accruing at 1.67 days per month. Leave can be taken after completing 3 months of employment.

Unused leave can be carried forward up to 5 days into the next year. Any excess will be forfeited unless approved by management for exceptional circumstances.

Sick Leave
Employees are entitled to 10 days of paid sick leave annually. No medical certificate required for absences up to 2 consecutive days.

For absences exceeding 2 days, a medical certificate must be submitted within 48 hours of return. Sick leave does not carry forward to the next year.

Public Holidays
We observe all national public holidays. If a public holiday falls on a weekend, the following Monday is observed as a holiday.

Employees working on public holidays receive double pay or compensatory time off, subject to prior approval from their manager.

Parental Leave
Primary caregivers receive 16 weeks of paid parental leave. Secondary caregivers receive 4 weeks. Leave must be taken within 12 months of birth or adoption.

Employees can request flexible return-to-work arrangements including reduced hours or remote work for up to 6 months after returning.

Leave Application Process
Submit leave requests through the HR portal at least 2 weeks in advance for planned leave. Emergency leave can be requested via email to your manager and HR.

Approval is subject to business needs and team coverage. You'll receive confirmation within 3 business days.
""",

    "hr/benefits_guide.txt": """Employee Benefits Guide

Health Insurance
We provide comprehensive health insurance covering medical, dental, and vision care. Coverage begins on your first day of employment.

The company covers 80% of premiums for employees and 60% for dependents. You can add spouse and children to your plan during enrollment or within 30 days of a qualifying life event.

Retirement Plan
We offer a 401(k) retirement plan with company matching up to 5% of your salary. You're eligible to enroll after 3 months of employment.

Company contributions vest over 4 years at 25% per year. You can adjust your contribution percentage anytime through the benefits portal.

Wellness Programs
Access to mental health support through our Employee Assistance Program (EAP) including 6 free counseling sessions per year.

Gym membership reimbursement up to $50/month. Annual health screenings and flu shots provided on-site or reimbursed.

Stock Options
Eligible employees receive stock options as part of compensation packages. Options vest over 4 years with a 1-year cliff.

You'll receive detailed grant information including strike price, vesting schedule, and exercise windows in your offer letter.

Additional Perks
Home office stipend of $500 for remote employees. Monthly internet reimbursement of $75. Company laptop and necessary equipment provided.

Free snacks and beverages in office locations. Team building events and social activities throughout the year.
""",

    "hr/performance_management.txt": """Performance Management System

Performance Review Cycle
We conduct formal performance reviews twice annually in June and December. Reviews assess goal achievement, competencies, and overall contribution.

Your manager will schedule a review meeting to discuss feedback, accomplishments, and development areas. Reviews inform compensation decisions and promotion eligibility.

Goal Setting Process
At the start of each review period, you'll work with your manager to set SMART goals aligned with team and company objectives.

Goals should be specific, measurable, achievable, relevant, and time-bound. Typically 3-5 major goals per period with clear success criteria.

Continuous Feedback
We encourage ongoing feedback rather than waiting for formal reviews. Managers should provide regular check-ins at least monthly.

Peers can provide feedback anytime through the 360-feedback tool. Constructive feedback should be specific, timely, and actionable.

Performance Improvement Plans
If performance falls below expectations, your manager will work with you on a Performance Improvement Plan (PIP) outlining specific areas for improvement.

PIPs typically run 60-90 days with clear milestones and support resources. Regular check-ins track progress and provide guidance.

Career Development
Discuss career aspirations during performance reviews. We support internal mobility and provide pathways for both individual contributor and management tracks.

Promotion criteria include sustained high performance, demonstrated readiness for next level, and business need. Promotions are reviewed quarterly.
""",

    "hr/employee_conduct.txt": """Code of Conduct and Professional Standards

Professional Behavior
Treat all colleagues, clients, and partners with respect and professionalism. Discrimination, harassment, or bullying of any kind will not be tolerated.

Maintain confidentiality of sensitive company and customer information. Use company resources responsibly and for business purposes.

Workplace Harassment Policy
We are committed to providing a harassment-free workplace. Harassment includes unwelcome conduct based on protected characteristics including race, gender, religion, age, or disability.

Sexual harassment, including unwanted advances, inappropriate comments, or creating a hostile environment, is strictly prohibited.

Reporting Violations
Report any violations of this code to your manager, HR, or through our anonymous ethics hotline. All reports are investigated promptly and confidentially.

Retaliation against anyone who reports concerns in good faith is prohibited and will result in disciplinary action.

Conflicts of Interest
Disclose any potential conflicts of interest including outside employment, financial interests in competitors or vendors, or personal relationships with colleagues in reporting lines.

Approval may be required for certain outside activities. When in doubt, consult with HR.

Social Media Guidelines
You're welcome to mention your employment on social media, but make clear that views expressed are your own, not the company's.

Don't share confidential information, disparage the company or colleagues, or engage in harassment online. Represent the company professionally.

Disciplinary Process
Violations may result in disciplinary action ranging from verbal warning to termination, depending on severity. Serious violations may result in immediate termination.

Employees have the right to respond to allegations and present their perspective during investigations.
""",

    "hr/hiring_process.txt": """Hiring and Recruitment Process

Requisition Approval
Hiring managers submit job requisitions through the HR portal including role description, level, budget, and business justification.

Requisitions are reviewed by department heads and HR for approval. Once approved, the role is posted internally for 5 days before external posting.

Interview Process
Our standard process includes: phone screen (30 min), technical/skills assessment (60-90 min), team interviews (2-3 rounds), and final interview with hiring manager.

All interviewers complete bias training and use structured interview guides. We aim to complete the process within 3 weeks of application.

Candidate Evaluation
Interviewers submit feedback within 24 hours using our standardized rubric. Hiring decisions are made collectively considering all feedback.

We evaluate technical skills, cultural fit, communication, problem-solving, and growth potential. References are checked before extending offers.

Offer Process
HR prepares offer letters including compensation, benefits, start date, and any conditions. Offers require approval from hiring manager and department head.

Candidates typically have 5-7 business days to accept. We're happy to answer questions and negotiate within approved parameters.

Onboarding Preparation
Once offer is accepted, HR initiates background check and prepares onboarding materials. IT provisions equipment and accounts.

New hire's manager prepares 30-60-90 day plan and assigns an onboarding buddy. First day agenda includes orientation, system setup, and team introductions.

Internal Mobility
Current employees are encouraged to apply for internal openings. Internal candidates are given priority consideration if qualifications match.

Managers should support employee growth and not block internal transfers. Transition timeline is negotiated between current and future managers.
""",

    "hr/onboarding_guide.txt": """New Employee Onboarding Guide

Before Your First Day
You'll receive a welcome email with your start date, time, location (or video link), and what to bring. Complete any pre-employment paperwork sent by HR.

Your laptop and equipment will be shipped to arrive before your start date. Don't open the box - we'll set it up together on day one.

First Day Agenda
Your first day starts at 10 AM with HR orientation covering benefits, policies, and systems. You'll complete required paperwork and receive your employee ID.

Meet your manager and team, get your workspace set up, and have lunch with your onboarding buddy. End the day with a welcome meeting with your department head.

First Week Goals
Complete all required training modules including security awareness, code of conduct, and system tutorials. Set up your development environment and tools.

Schedule 1-on-1 meetings with key team members and stakeholders. Review your 30-60-90 day plan with your manager.

30-60-90 Day Plan
First 30 days: Learn systems, processes, and team dynamics. Complete onboarding tasks and shadow team members. Start contributing to small projects.

Days 31-60: Take ownership of specific tasks and projects. Begin participating in team meetings and decision-making. Seek feedback regularly.

Days 61-90: Operate independently on assigned work. Contribute ideas and improvements. Complete first performance check-in with manager.

Onboarding Buddy Program
Your buddy is a peer who will help you navigate the company, answer questions, and provide informal support during your first 90 days.

Schedule regular check-ins with your buddy. They're your go-to for questions about culture, unwritten rules, and day-to-day operations.

Resources and Support
Access the employee portal for policies, forms, and resources. Join relevant Slack channels for your team and interests.

HR is available for questions about benefits, policies, or concerns. Your manager is your primary point of contact for work-related questions.
""",

    "hr/payroll_faq.txt": """Payroll Frequently Asked Questions

When Do I Get Paid?
Payroll is processed bi-weekly on Fridays. If payday falls on a holiday, payment is processed the business day before.

Direct deposit typically arrives by 9 AM on payday. Paper checks are available upon request but may take additional processing time.

How Do I Update Direct Deposit?
Log into the HR portal and navigate to Payroll > Direct Deposit. You can add, edit, or remove bank accounts.

Changes must be submitted at least 5 business days before the next pay period to take effect. You'll receive confirmation once processed.

Understanding Your Payslip
Your payslip shows gross pay, deductions (taxes, benefits, retirement), and net pay. Year-to-date totals are included for tax purposes.

Pre-tax deductions include health insurance and 401(k) contributions. Post-tax deductions include any garnishments or voluntary contributions.

Tax Withholding
Update your W-4 tax withholding anytime through the HR portal. Changes take effect in the next pay period.

Consult a tax professional if you're unsure about appropriate withholding. The company cannot provide tax advice.

Overtime and Time Tracking
Non-exempt employees must track hours worked and submit timesheets by end of day Friday for that week's pay period.

Overtime (over 40 hours/week) is paid at 1.5x regular rate. All overtime must be pre-approved by your manager.

Payroll Errors
If you notice an error in your paycheck, contact HR immediately. We'll investigate and issue corrections within 2 business days.

For underpayments, we'll process an off-cycle payment. Overpayments will be deducted from future paychecks unless other arrangements are made.

Year-End Tax Documents
W-2 forms are available by January 31st each year through the HR portal. You'll receive an email notification when available.

Keep your mailing address current in the system to ensure you receive any required paper copies.
""",

    "hr/grievance_policy.txt": """Employee Grievance and Complaint Policy

Purpose and Scope
This policy provides a fair and transparent process for employees to raise concerns about workplace issues, treatment, or policy violations.

All employees have the right to raise grievances without fear of retaliation. We are committed to resolving issues promptly and fairly.

Informal Resolution
We encourage employees to first attempt informal resolution by discussing concerns directly with the involved party or their immediate manager.

Many issues can be resolved through open communication. Your manager can facilitate discussions or provide guidance on next steps.

Formal Grievance Process
If informal resolution is unsuccessful or inappropriate, submit a written grievance to HR including details of the issue, parties involved, and desired resolution.

HR will acknowledge receipt within 2 business days and begin investigation. You may be asked to provide additional information or documentation.

Investigation Procedure
HR will conduct a thorough and impartial investigation, interviewing relevant parties and reviewing documentation. Investigations typically complete within 15 business days.

All parties are expected to cooperate fully and maintain confidentiality. Findings and recommended actions will be documented.

Resolution and Appeal
You'll receive written notification of the investigation outcome and any actions taken. If you're unsatisfied with the resolution, you may appeal to the department head within 10 days.

Appeals are reviewed by senior leadership and HR. The appeal decision is final.

Protection from Retaliation
Retaliation against anyone who raises a grievance in good faith is strictly prohibited and will result in disciplinary action up to termination.

If you experience retaliation, report it immediately to HR or use the anonymous ethics hotline.

Confidentiality
Grievances are handled confidentially to the extent possible. Information is shared only with those who need to know for investigation and resolution purposes.

All parties involved are expected to maintain confidentiality throughout the process.
""",

    "hr/remote_work_policy.txt": """Remote Work Policy

Eligibility and Approval
Remote work is available to employees whose roles can be performed effectively outside the office. Approval is at manager's discretion based on role requirements and performance.

New employees typically work on-site or hybrid for the first 90 days to facilitate onboarding and team integration.

Work Environment Requirements
Remote employees must have a dedicated workspace with reliable high-speed internet (minimum 25 Mbps download, 5 Mbps upload).

Workspace should be quiet, professional, and free from distractions during work hours. Ensure proper ergonomics to prevent injury.

Equipment and Technology
The company provides laptop, monitor, keyboard, mouse, and necessary software. Additional equipment may be approved based on role requirements.

Home office stipend of $500 provided for desk, chair, and other setup needs. Monthly internet reimbursement of $75.

Communication and Availability
Remote employees must be available during core hours (10 AM - 4 PM local time) for meetings and collaboration. Keep your Slack status updated.

Respond to messages and emails within expected timeframes. Use video for team meetings to maintain connection and engagement.

Security Requirements
Follow all IT security policies including VPN usage, password management, and data protection. Never share login credentials or leave devices unattended.

Ensure your home network is secured with WPA2 or WPA3 encryption. Install company-approved security software and keep systems updated.

Performance Expectations
Remote work is a privilege contingent on maintaining performance standards. Managers will evaluate productivity, communication, and collaboration.

If performance issues arise, remote work privileges may be modified or revoked. Regular check-ins ensure alignment and address concerns early.

Hybrid Work Arrangements
Hybrid employees split time between office and remote work. Coordinate with your team to ensure adequate coverage and collaboration opportunities.

Office days should be used for meetings, team activities, and work requiring in-person collaboration. Remote days for focused individual work.

Travel and Relocation
If you plan to work remotely from a different location temporarily (more than 2 weeks), notify your manager and HR for approval.

Permanent relocation may affect compensation based on location. Discuss with HR before making relocation decisions.
""",

    "it/acceptable_use_policy.txt": """Acceptable Use Policy

Purpose and Scope
This policy defines acceptable use of company IT resources including computers, networks, email, internet, and software. All employees must comply.

Company resources are provided for business purposes. Limited personal use is permitted if it doesn't interfere with work or violate policies.

Prohibited Activities
Do not use company resources for illegal activities, harassment, discrimination, or accessing inappropriate content including pornography or hate speech.

Prohibited: Installing unauthorized software, attempting to bypass security controls, sharing credentials, or accessing systems without authorization.

Email and Communication
Company email is for business communication. Personal use should be minimal. All email is company property and may be monitored.

Use professional language and tone. Don't send confidential information to personal email accounts. Be cautious of phishing attempts.

Internet Usage
Internet access is provided for work-related research and communication. Streaming video or music should be limited to breaks and not impact bandwidth.

Don't visit malicious or inappropriate websites. Use company VPN when accessing company resources from outside networks.

Software and Applications
Only install software approved by IT. Unauthorized software may contain malware or violate licensing agreements.

Request software through the IT portal. Open source software requires security review before use. Keep all software updated.

Data and File Management
Store work files on company-approved cloud storage or network drives, not local devices. Follow data classification and retention policies.

Don't download or store illegal, offensive, or confidential content inappropriately. Regularly backup important files.

Mobile Devices
Company-issued mobile devices must have passcodes enabled and security software installed. Report lost or stolen devices immediately.

Personal devices accessing company email or data must comply with mobile device management (MDM) policies.

Monitoring and Privacy
The company reserves the right to monitor use of IT resources to ensure policy compliance and security. Employees have limited privacy expectations.

Monitoring may include email, internet activity, and file access. Monitoring is conducted in accordance with applicable laws.

Violations and Consequences
Policy violations may result in disciplinary action up to termination. Serious violations may be reported to law enforcement.

If you're unsure whether an activity is permitted, contact IT or your manager before proceeding.
""",

    "it/security_policy.txt": """Information Security Policy

Security Principles
Protect company and customer data through confidentiality, integrity, and availability. Security is everyone's responsibility.

Follow the principle of least privilege - access only what you need for your role. Report security concerns immediately.

Access Control
User accounts are personal and non-transferable. Never share passwords or login credentials. Use strong, unique passwords for each system.

Multi-factor authentication (MFA) is required for all systems. Access is granted based on role and revoked upon termination or role change.

Password Requirements
Passwords must be at least 12 characters with uppercase, lowercase, numbers, and special characters. Don't reuse passwords across systems.

Change passwords immediately if compromised. Use the company password manager to generate and store passwords securely.

Data Classification
Data is classified as Public, Internal, Confidential, or Restricted. Handle data according to its classification level.

Confidential and Restricted data requires encryption in transit and at rest. Don't store sensitive data on personal devices or unauthorized cloud services.

Physical Security
Lock your computer when leaving your desk. Don't leave devices unattended in public places. Secure printed confidential documents.

Visitors must be escorted in office areas. Report tailgating or unauthorized persons to security immediately.

Incident Reporting
Report security incidents including suspected malware, phishing, data breaches, or policy violations to security@company.com immediately.

Don't attempt to investigate or remediate incidents yourself. Preserve evidence and follow security team instructions.

Remote Access
Use company VPN for all remote access to company resources. Don't access company systems from public or unsecured networks without VPN.

Ensure your home network is secured. Don't allow others to use company devices or access company systems through your credentials.

Third-Party Security
Vendors and partners with access to company systems or data must comply with our security requirements and sign appropriate agreements.

Don't share company data with third parties without proper authorization and data protection agreements.

Security Training
All employees must complete annual security awareness training. Additional role-specific training may be required.

Stay informed about current threats and security best practices. When in doubt, ask the security team.

Compliance and Audits
Comply with all security audits and assessments. Provide requested information and access to auditors promptly.

Security policies are reviewed annually and updated as needed. You'll be notified of significant changes.
""",

    "it/incident_response.txt": """IT Incident Response Procedure

Incident Classification
Incidents are classified by severity: P1 (Critical - system down), P2 (High - major functionality impaired), P3 (Medium - minor impact), P4 (Low - minimal impact).

Response time SLAs: P1 - 15 minutes, P2 - 1 hour, P3 - 4 hours, P4 - next business day. Escalation occurs if SLAs are not met.

Incident Detection and Reporting
Incidents may be detected through monitoring alerts, user reports, or security scans. Report incidents via IT helpdesk portal, email, or phone.

Provide detailed information: what happened, when, who's affected, error messages, and steps to reproduce. Screenshots are helpful.

Initial Response
On-call engineer acknowledges incident and begins triage. Assess severity, impact, and urgency. Notify stakeholders if customer-facing systems are affected.

Create incident ticket with all relevant details. Begin investigation to identify root cause. Implement temporary workarounds if possible.

Escalation Procedures
Escalate to senior engineers or specialists if incident cannot be resolved within SLA timeframe or requires specialized expertise.

For P1 incidents, notify incident commander and assemble response team. Establish communication bridge for coordination.

Communication During Incidents
Post status updates in #incidents Slack channel every 30 minutes for P1/P2, hourly for P3. Update incident ticket with progress.

Notify affected users through status page. Provide estimated time to resolution when known. Be transparent about impact and progress.

Resolution and Recovery
Once root cause is identified, implement fix and verify resolution. Monitor systems to ensure stability. Document resolution steps.

Conduct post-incident review within 48 hours for P1/P2 incidents. Identify lessons learned and preventive actions.

Post-Incident Review
Review timeline, root cause, impact, and response effectiveness. Identify what went well and areas for improvement.

Create action items to prevent recurrence. Update runbooks and documentation. Share learnings with broader team.

Documentation Requirements
All incidents must be fully documented including timeline, actions taken, root cause, and resolution. Update knowledge base with solutions.

Maintain incident metrics for trend analysis and continuous improvement. Report major incidents to leadership.
""",

    "it/vpn_usage.txt": """VPN Usage Guidelines

When to Use VPN
Always use company VPN when accessing company resources from outside the office network. This includes email, file shares, internal applications, and databases.

VPN is required when working from home, coffee shops, hotels, or any non-company network. Public WiFi networks are particularly risky without VPN.

VPN Client Installation
Download the approved VPN client from the IT portal. Installation guides are available for Windows, Mac, Linux, iOS, and Android.

Contact IT helpdesk if you encounter installation issues. VPN client must be kept updated to latest version for security patches.

Connecting to VPN
Launch VPN client and enter your company credentials. Enable multi-factor authentication when prompted. Select appropriate VPN gateway for your region.

Connection typically establishes within 30 seconds. Green indicator shows successful connection. All traffic is now encrypted and routed through company network.

Split Tunnel vs Full Tunnel
Our VPN uses split tunneling - only company traffic goes through VPN, personal traffic uses your regular internet connection.

This improves performance for personal browsing while securing company data. Don't attempt to modify tunnel configuration.

VPN Performance
VPN may slightly reduce internet speed due to encryption overhead. If experiencing significant slowness, try different VPN gateway or check your internet connection.

Disconnect and reconnect if VPN becomes unresponsive. Contact IT if problems persist.

Troubleshooting Common Issues
Cannot connect: Verify internet connection, check credentials, ensure MFA device is available. Try different network if on public WiFi.

Frequent disconnections: Check for VPN client updates, verify network stability, contact IT if issue continues.

Slow performance: Try different VPN gateway, close unnecessary applications, check local network speed.

Security Considerations
Never disable VPN to access company resources faster. Don't share VPN credentials. Report suspicious VPN activity to security team.

VPN logs are monitored for security purposes. Unusual patterns may trigger security review.

Mobile VPN Usage
Install VPN profile on mobile devices accessing company email or data. VPN should auto-connect when accessing company resources.

Keep VPN app updated. Battery usage may increase when VPN is active. Disconnect when not accessing company resources to save battery.

VPN for Travel
When traveling internationally, connect to VPN before accessing company resources. Some countries restrict VPN usage - check local laws.

VPN may be slower due to distance from gateways. Plan accordingly for time-sensitive work.
""",

    "it/password_policy.txt": """Password Security Policy

Password Requirements
Minimum 12 characters including uppercase, lowercase, numbers, and special characters. Avoid common words, personal information, or sequential patterns.

Passwords expire every 90 days. Cannot reuse last 10 passwords. System will prompt you to change password 7 days before expiration.

Password Manager Usage
Use company-provided password manager (1Password) to generate and store passwords. Password manager is required for all employees.

Generate random passwords of 16+ characters for maximum security. Password manager syncs across devices and auto-fills credentials.

Multi-Factor Authentication
MFA is required for all company systems. Use authenticator app (preferred) or SMS for second factor. Hardware tokens available upon request.

Backup MFA codes are provided during setup - store securely. Contact IT immediately if you lose access to MFA device.

Password Storage
Never write passwords down or store in plain text files. Don't save passwords in browsers unless using company password manager.

Don't share passwords via email, Slack, or text message. Use secure sharing features in password manager if needed.

Account Security
Enable MFA on personal accounts used for work (GitHub, AWS, etc.). Use unique passwords for each account - never reuse passwords.

Review account activity regularly for suspicious logins. Enable login notifications where available.

Compromised Passwords
Change password immediately if you suspect compromise. Notify IT security team. Review recent account activity for unauthorized access.

If company data may have been exposed, report as security incident. Don't attempt to investigate yourself.

Password Reset Process
Self-service password reset available through IT portal using security questions or MFA. Helpdesk can reset if self-service fails.

Identity verification required for helpdesk resets. New temporary password must be changed on first login.

Service Account Passwords
Service accounts require 20+ character randomly generated passwords. Store in password manager with restricted access.

Service account passwords don't expire but should be rotated annually or when personnel with access leave.

Third-Party Accounts
Use SSO (Single Sign-On) for third-party services when available. For services without SSO, follow same password requirements.

Don't use personal email for work-related third-party accounts. Use company email and password manager.

Password Audits
IT conducts periodic password audits to identify weak or compromised passwords. You'll be notified if your password needs changing.

Comply promptly with password change requests. Repeated non-compliance may result in account suspension.
""",

    "it/email_security.txt": """Email Security Best Practices

Phishing Awareness
Phishing emails attempt to steal credentials or install malware. Be suspicious of unexpected emails, especially with urgent requests or attachments.

Verify sender email address carefully - attackers often use similar-looking domains. Hover over links to see actual destination before clicking.

Identifying Suspicious Emails
Red flags: Urgent requests for credentials or money, poor grammar/spelling, generic greetings, mismatched sender/reply-to addresses.

Suspicious attachments: Unexpected files, unusual extensions (.exe, .zip, .scr), files from unknown senders.

Reporting Phishing
Forward suspicious emails to phishing@company.com. Don't click links or open attachments. IT will investigate and notify you of findings.

Reporting helps protect others. Even if you're unsure, report it - better safe than sorry.

Email Attachments
Scan attachments with antivirus before opening. Be especially cautious with executable files, macros, and compressed archives.

Don't open attachments from unknown senders. Verify unexpected attachments with sender through separate communication channel.

Link Safety
Hover over links to preview destination URL. Be wary of shortened URLs or links with misspellings. Don't click links in suspicious emails.

Type URLs directly into browser for sensitive sites like banking or company portals. Bookmark frequently used sites.

Email Encryption
Use email encryption for confidential or restricted data. Encryption option available in email client for sensitive messages.

Encrypted emails require recipient to authenticate before viewing. Use for financial data, personal information, or trade secrets.

Email Retention
Follow company retention policy - don't delete emails that may be needed for legal or business purposes. Auto-deletion applies after retention period.

Archive important emails for future reference. Don't use email as primary file storage - use approved document management systems.

External Email Warnings
Emails from external senders are tagged with warning banner. Exercise extra caution with external emails requesting action or information.

Verify requests through known contact information, not information in the email itself.

Business Email Compromise
CEO fraud and vendor impersonation are common. Verify unusual requests for wire transfers or sensitive data through phone call to known number.

Don't rely solely on email for financial transactions. Follow approval workflows and dual authorization requirements.

Email Forwarding
Don't auto-forward company email to personal accounts. This violates data protection policies and creates security risks.

Use email client's mobile app or webmail for remote access. Contact IT if you need email access on personal devices.

Spam and Unwanted Email
Mark spam using email client's spam button. Don't unsubscribe from suspicious emails - this confirms your address is active.

IT maintains spam filters but some may get through. Report persistent spam to IT for filter updates.
""",

    "it/cloud_access_standards.txt": """Cloud Access and Security Standards

Approved Cloud Services
Use only IT-approved cloud services listed in the IT portal. Approved services have undergone security review and have appropriate data protection agreements.

Request new cloud services through IT portal with business justification. Security review typically takes 5-10 business days.

Cloud Authentication
Use SSO (Single Sign-On) for cloud services when available. This provides centralized access control and MFA enforcement.

For services without SSO, use strong unique passwords stored in password manager. Enable MFA on all cloud accounts.

Data Storage in Cloud
Store company data only in approved cloud storage (Google Drive, SharePoint). Follow data classification guidelines for cloud storage.

Confidential and Restricted data requires encryption and access controls. Don't store sensitive data in personal cloud accounts.

Cloud Sharing and Collaboration
Share files using secure sharing links with expiration dates and access controls. Don't share confidential data with external parties without approval.

Review and revoke unnecessary sharing permissions regularly. Use view-only access when editing isn't required.

Cloud Application Security
Keep cloud applications updated. Review and minimize third-party app integrations. Revoke access for unused integrations.

Review cloud application permissions before granting access. Be cautious of apps requesting excessive permissions.

Shadow IT Prevention
Don't use unapproved cloud services for company work. Shadow IT creates security gaps and compliance risks.

If you need a tool not currently approved, request it through proper channels. IT will evaluate and approve if appropriate.

Cloud Access Monitoring
Cloud access is monitored for security and compliance. Unusual activity may trigger security review.

Access logs are retained per retention policy. Comply with access audits and reviews.

Cloud Data Backup
Company data in approved cloud services is automatically backed up. Don't rely solely on cloud provider's backup - maintain local copies of critical data.

Test data recovery periodically to ensure backups are functional.

Cloud Cost Management
Be mindful of cloud resource usage and costs. Delete unnecessary files and resources. Use cost allocation tags for departmental resources.

Review cloud spending reports. Optimize resource usage to control costs.

Offboarding and Access Revocation
Cloud access is revoked upon termination or role change. Transfer ownership of shared resources before departure.

Document cloud resources and access for knowledge transfer. Don't retain access to company cloud services after leaving.
""",

    "it/device_management.txt": """Device Management Policy

Company-Issued Devices
Company provides laptops and mobile devices as needed for your role. Devices remain company property and must be returned upon termination.

Standard laptop refresh cycle is 3 years. Request early replacement if device is failing or inadequate for your work.

Device Setup and Configuration
IT configures devices with required software, security tools, and settings before distribution. Don't remove or disable security software.

Additional software can be requested through IT portal. Keep devices updated with latest OS and security patches.

Mobile Device Management
Company-issued mobile devices are enrolled in MDM (Mobile Device Management). MDM enforces security policies and enables remote wipe if lost.

Personal devices accessing company email must install MDM profile. MDM only manages work data, not personal data.

Device Security Requirements
Enable full disk encryption on all devices. Use strong passwords/PINs. Enable biometric authentication where available.

Lock devices when unattended. Set auto-lock to 5 minutes or less. Never leave devices in vehicles or unsecured locations.

Lost or Stolen Devices
Report lost or stolen devices to IT immediately. IT will remotely lock and wipe device to protect company data.

File police report for stolen devices. Provide report number to IT for insurance purposes.

Personal Use of Company Devices
Limited personal use of company devices is permitted if it doesn't interfere with work or violate policies.

Personal data on company devices is not private and may be accessed during investigations. Don't store sensitive personal data on company devices.

Bring Your Own Device (BYOD)
Personal devices can access company email and approved cloud services with MDM profile installed.

BYOD devices must meet minimum security requirements: current OS, passcode enabled, encryption enabled, security updates current.

Device Maintenance
Keep devices clean and in good condition. Report hardware issues to IT promptly. Don't attempt repairs yourself.

Backup important data regularly. Use approved cloud storage or network drives, not local storage only.

Software Installation
Install only IT-approved software. Request software through IT portal. Unauthorized software may be removed during security scans.

Keep all software updated. Enable automatic updates where possible. Don't disable or postpone critical security updates.

Device Return Process
Upon termination or device replacement, return device to IT within 3 business days. Backup personal data before return.

IT will wipe device and verify all company data is removed. Accessories (charger, case, etc.) must also be returned.

Remote Work Device Requirements
Remote workers receive same device standards as office workers. Ensure adequate workspace for device setup.

Use surge protector for desktop equipment. Maintain proper ventilation to prevent overheating.
""",

    "it/data_retention.txt": """Data Retention and Disposal Policy

Retention Periods
Email: 7 years. Financial records: 7 years. HR records: 7 years post-employment. Contracts: 7 years post-expiration.

Project documents: 3 years post-completion. General business records: 3 years. Marketing materials: 1 year.

Legal Hold
Data subject to legal hold must be preserved regardless of retention period. Legal team will notify of legal holds.

Don't delete or modify data under legal hold. Contact legal team with questions about legal hold scope.

Data Classification and Retention
Retention periods vary by data classification. Restricted data may have longer retention due to regulatory requirements.

Consult data classification guide for specific retention requirements. When in doubt, contact compliance team.

Email Retention
Email is automatically archived after 90 days. Archived email remains searchable and accessible. Auto-deletion occurs after retention period.

Don't use personal email for business communication - it's not captured by retention systems.

File Storage Retention
Files on network drives and cloud storage are retained per policy. Inactive files may be archived to reduce storage costs.

Organize files logically and delete obsolete files. Don't hoard unnecessary data.

Backup Retention
Daily backups retained for 30 days. Weekly backups retained for 90 days. Monthly backups retained for 1 year.

Backups are for disaster recovery, not long-term archival. Use proper document management for long-term retention.

Data Disposal
Data disposal must ensure data cannot be recovered. Use secure deletion tools for electronic data. Shred physical documents.

IT handles disposal of devices and media. Don't throw devices in regular trash.

End of Life Data
When systems are decommissioned, data is migrated or securely deleted. Stakeholders are notified before decommissioning.

Verify data migration completeness before old system deletion. Retain system documentation per retention policy.

Personal Data Retention
Personal data (employee, customer) is retained only as long as needed for business or legal purposes.

Comply with data subject requests for deletion (right to be forgotten) unless legal obligation requires retention.

Retention Compliance
Compliance team audits retention practices annually. Departments must demonstrate compliance with retention policies.

Violations may result in legal or regulatory penalties. Report retention concerns to compliance team.
""",

    "it/software_approval_process.txt": """Software Approval and Licensing

Software Request Process
Submit software requests through IT portal including software name, purpose, cost, and business justification.

IT evaluates requests for security, compatibility, licensing, and business need. Approval typically takes 3-5 business days.

Security Review
All software undergoes security review before approval. Review includes vulnerability assessment, vendor reputation, and data handling practices.

Open source software requires additional review of license terms and community support. Some licenses may not be compatible with commercial use.

Licensing Compliance
Use only properly licensed software. Don't install personal licenses on company devices or use company licenses on personal devices.

Track license usage to ensure compliance. Unused licenses should be reclaimed and reassigned.

Approved Software List
Consult approved software list in IT portal before requesting new software. Approved software has completed security review and has active licenses.

Standard software is pre-installed on company devices. Request installation of approved software through IT portal.

Prohibited Software
Don't install: Pirated software, peer-to-peer file sharing, remote access tools (except approved), cryptocurrency miners, or software from untrusted sources.

Prohibited software will be removed if detected. Violations may result in disciplinary action.

Software Updates
Keep all software updated to latest stable version. Enable automatic updates where possible. Critical security updates are mandatory.

IT may push updates remotely for security patches. Don't disable or postpone critical updates.

Cloud Software and SaaS
Cloud software requests follow same approval process. Additional considerations: data residency, vendor security practices, integration requirements.

Use SSO for cloud software when available. Ensure proper offboarding procedures for cloud access.

Open Source Software
Open source software requires review of license terms (GPL, MIT, Apache, etc.). Some licenses have restrictions on commercial use or require source code disclosure.

Evaluate community support and update frequency. Abandoned projects pose security risks.

Software License Management
IT maintains software license inventory. License audits conducted annually. Ensure you're using assigned licenses correctly.

Report unused software for license reclamation. Don't share licenses or install on multiple devices unless license permits.

Vendor Management
Software vendors must complete security questionnaire and sign data protection agreements. Vendor risk is assessed based on data access and criticality.

Maintain vendor contact information for support and security notifications.

Trial Software
Trial software requires same approval as purchased software. Trials must have defined evaluation period and decision criteria.

Remove trial software after evaluation period if not purchasing. Don't use trial software for production work.
""",

    "finance/expense_guidelines.txt": """Employee Expense Guidelines

Expense Policy Overview
Employees may incur reasonable business expenses with proper approval. All expenses must be business-related, necessary, and properly documented.

Submit expense reports within 30 days of incurring expense. Late submissions may not be reimbursed.

Approval Requirements
Expenses under $500: Manager approval. $500-$2000: Department head approval. Over $2000: VP approval required before incurring expense.

Pre-approval required for travel, conferences, and large purchases. Emergency expenses can be approved retroactively with justification.

Eligible Expenses
Business travel (flights, hotels, ground transportation), client entertainment, office supplies, professional development, business meals.

Home office equipment (with approval), internet reimbursement for remote workers, mobile phone reimbursement.

Ineligible Expenses
Personal expenses, alcohol (except client entertainment with approval), traffic violations, personal travel, gym memberships (except wellness program).

First-class travel (except international flights over 6 hours), luxury accommodations, excessive meal costs.

Receipt Requirements
Receipts required for all expenses over $25. Digital photos of receipts acceptable. Credit card statements alone are not sufficient.

Receipts must show: Date, vendor, amount, items purchased. Missing receipts require written explanation and manager approval.

Expense Categories
Travel: Flights, hotels, rental cars, parking, tolls, taxis/rideshare. Meals: Business meals, client entertainment. Supplies: Office supplies, equipment.

Professional Development: Courses, conferences, books, certifications. Other: Specify in expense report with explanation.

Per Diem Rates
Domestic travel: $75/day for meals. International travel: Varies by location, see finance portal for rates.

Per diem covers meals and incidentals. Receipts not required for per diem. Cannot claim both per diem and actual meal expenses.

Corporate Credit Cards
Corporate cards issued to frequent travelers and managers. Use for business expenses only. Submit expense reports monthly even if using corporate card.

Personal charges on corporate card must be reimbursed immediately. Repeated misuse may result in card revocation.

Reimbursement Timeline
Expense reports processed within 10 business days of approval. Reimbursement via direct deposit to payroll account.

Incomplete or improperly documented reports will be rejected with explanation. Correct and resubmit promptly.

Currency and Exchange Rates
International expenses should be submitted in original currency. System automatically converts using exchange rate on transaction date.

Keep currency conversion receipts for large expenses. Credit card exchange rates are acceptable for small purchases.

Mileage Reimbursement
Personal vehicle use for business reimbursed at IRS standard rate (currently $0.655/mile). Submit mileage log with start/end locations and business purpose.

Commuting miles not reimbursable. Only business miles beyond normal commute are eligible.
""",

    "finance/travel_policy.txt": """Business Travel Policy

Travel Approval
All business travel requires advance approval. Submit travel request through finance portal at least 2 weeks before travel.

Include: Destination, dates, purpose, estimated costs. Approval required from manager and finance for international travel.

Booking Travel
Use company travel portal for flights and hotels to get corporate rates. Book economy class for domestic flights, premium economy for international over 6 hours.

Book refundable fares when possible for flexibility. Travel insurance included for international trips.

Flight Guidelines
Book flights 3-4 weeks in advance for best rates. Direct flights preferred when cost difference is less than $200.

Reasonable departure times (not red-eyes unless necessary). Baggage fees reimbursed for checked bags (up to 2 bags).

Hotel Accommodations
Book hotels within $200/night in major cities, $150/night in other locations. Higher rates require approval with justification.

Use corporate hotel partners when available for discounts. Extended stays may qualify for apartment rentals (more economical).

Ground Transportation
Use public transportation, rideshare, or taxis. Rental cars approved for locations without adequate public transit or when more economical.

Book compact or mid-size rental cars. Upgrade to larger vehicle only if needed for multiple passengers or equipment.

Meals and Entertainment
Reasonable meal expenses reimbursed with receipts. Client entertainment requires pre-approval and business justification.

Alcohol reimbursed only for client entertainment, not personal meals. Tip 15-20% for good service.

International Travel
Passport and visa costs reimbursed for business travel. Apply for visas well in advance (6-8 weeks).

Review travel advisories and health requirements. Company travel insurance covers medical emergencies and evacuation.

Travel Advances
Travel advances available for international trips or extended domestic travel. Request through finance portal at least 1 week before travel.

Reconcile advance with expense report within 2 weeks of return. Repay unused advance or submit expenses to cover advance.

Combining Business and Personal Travel
Personal days can be added to business trips at your expense. Book business portion separately or calculate business vs personal costs.

Company only reimburses business portion of expenses. Additional personal travel days don't extend per diem eligibility.

Travel Safety
Register international travel with security team. Provide emergency contact information. Check in with manager upon arrival.

Follow local laws and customs. Use hotel safes for valuables. Be aware of surroundings, especially in unfamiliar areas.

Frequent Flyer Programs
Keep frequent flyer miles and hotel points earned on business travel. Use points for personal travel or upgrade business travel at no cost to company.

Don't book more expensive flights just to earn miles. Business value takes priority over personal rewards.

Travel Expense Reporting
Submit travel expense report within 1 week of return. Include all receipts and itemized expenses.

Separate business and personal expenses clearly. Provide business purpose and attendees for entertainment expenses.
""",

    "finance/budget_approval.txt": """Budget and Expenditure Approval Process

Annual Budget Planning
Department budgets prepared in Q4 for following fiscal year. Department heads submit budget proposals including headcount, operations, and capital expenses.

Finance reviews proposals with department heads. Final budget approved by executive team and board in December.

Budget Categories
Personnel: Salaries, benefits, bonuses, contractors. Operations: Software, supplies, travel, training. Capital: Equipment, furniture, major purchases over $5000.

Marketing: Campaigns, events, advertising. R&D: Research, prototypes, testing. Facilities: Rent, utilities, maintenance.

Approval Thresholds
Under $1000: Manager approval. $1000-$5000: Department head approval. $5000-$25000: VP approval. Over $25000: CFO approval.

Unbudgeted expenses over $10000 require executive approval regardless of amount.

Purchase Requisition Process
Submit purchase requisition through finance portal with vendor, amount, budget code, and business justification.

Attach quotes from at least 2 vendors for purchases over $5000. Approval routing based on amount and budget availability.

Budget Tracking
Managers receive monthly budget reports showing spend vs budget. Review reports for accuracy and address variances.

Finance portal provides real-time budget visibility. Monitor spending throughout year to avoid overruns.

Budget Transfers
Transfer budget between categories within department with department head approval. Transfers between departments require VP approval.

Submit transfer request with justification. Transfers processed within 3 business days.

Unbudgeted Expenses
Unbudgeted expenses require special approval and justification. Identify funding source (budget surplus, contingency, or budget increase).

Emergency expenses can be approved quickly with executive approval. Document business need and impact of not approving.

Capital Expenditures
Capital expenses (over $5000, useful life over 1 year) require capital approval process. Submit capital request with ROI analysis and alternatives considered.

Capital budget reviewed quarterly. Approved capital projects tracked separately from operational budget.

Budget Amendments
Budget amendments for significant changes require executive approval. Submit amendment request with revised forecast and explanation of changes.

Amendments typically processed quarterly. Mid-year amendments for urgent needs can be expedited.

Vendor Selection
Competitive bidding required for purchases over $10000. Obtain at least 3 quotes. Select vendor based on price, quality, and service.

Existing vendor relationships and strategic partnerships may justify sole-source procurement with approval.

Contract Approval
Contracts require legal review before signing. Finance reviews contracts for budget impact and payment terms.

Signature authority based on contract value: Under $25000: Department head. $25000-$100000: VP. Over $100000: CFO or CEO.

Budget Variance Analysis
Significant variances (over 10% or $5000) require explanation. Submit variance analysis with corrective actions.

Favorable variances may allow budget reallocation. Unfavorable variances may require spending freeze or budget cut.
""",

    "finance/procurement_process.txt": """Procurement and Purchasing Process

Procurement Overview
Procurement ensures we get best value while maintaining quality and compliance. All purchases must follow procurement process.

Centralized procurement for common items (office supplies, equipment). Decentralized for specialized departmental needs.

Purchase Request
Submit purchase request through procurement portal with item description, quantity, estimated cost, and business justification.

Include preferred vendor if applicable. Attach specifications or requirements document for technical purchases.

Vendor Evaluation
Procurement evaluates vendors on price, quality, delivery time, service, and financial stability. New vendors complete vendor registration and due diligence.

Preferred vendor list maintained for common purchases. Using preferred vendors expedites approval process.

Competitive Bidding
Purchases over $10000 require competitive bidding. Procurement solicits quotes from at least 3 qualified vendors.

Evaluation criteria: Price (40%), quality (30%), delivery (15%), service (15%). Award to vendor with best overall value.

Purchase Orders
Approved purchases generate purchase order (PO). PO sent to vendor as authorization to deliver goods/services.

Don't commit to purchases without approved PO. Vendors should not deliver without valid PO number.

Receiving and Inspection
Receiving department inspects deliveries for quantity and quality. Report discrepancies or damage immediately.

Sign delivery receipt only after inspection. Receiving report sent to procurement and finance for payment processing.

Invoice Processing
Vendors submit invoices to accounts payable. Invoices matched to PO and receiving report (3-way match).

Discrepancies resolved before payment. Payment terms typically net 30 days. Early payment discounts taken when beneficial.

Emergency Purchases
Emergency purchases (system down, safety issue) can be expedited. Obtain verbal approval from authorized approver.

Submit formal purchase request within 24 hours. Document emergency nature and business impact.

Software and SaaS Procurement
Software purchases require IT approval for technical compatibility and security. SaaS agreements reviewed for data protection and terms.

Consider total cost of ownership including implementation, training, and ongoing support. Evaluate alternatives including open source.

Contract Negotiation
Procurement negotiates terms with vendors for large purchases. Legal reviews contracts before signing.

Negotiate: Price, payment terms, delivery schedule, warranties, support, termination clauses. Document negotiation outcomes.

Supplier Relationship Management
Maintain positive relationships with key suppliers. Conduct annual supplier reviews for strategic vendors.

Address performance issues promptly. Recognize excellent supplier performance. Diversify suppliers to reduce risk.

Procurement Compliance
Follow procurement policies and approval thresholds. Don't split purchases to avoid approval requirements.

Conflicts of interest must be disclosed. Don't accept gifts or favors from vendors beyond nominal value ($50).
""",

    "finance/vendor_management.txt": """Vendor Management Policy

Vendor Onboarding
New vendors complete registration form with business information, tax ID, banking details, and insurance certificates.

Procurement conducts due diligence: Credit check, reference checks, background check for high-risk vendors. Approval takes 5-10 business days.

Vendor Categories
Strategic vendors: Critical to operations, high spend, long-term relationship. Preferred vendors: Qualified vendors with favorable terms.

Approved vendors: Completed onboarding, available for use. Restricted vendors: Do not use without special approval.

Vendor Agreements
Master service agreements (MSA) for ongoing relationships. Statements of work (SOW) for specific projects.

Agreements include: Scope, pricing, payment terms, deliverables, SLAs, confidentiality, liability, termination. Legal review required.

Vendor Performance Monitoring
Track vendor performance: Quality, timeliness, responsiveness, compliance. Conduct quarterly reviews for strategic vendors.

Performance issues addressed through corrective action plans. Persistent issues may result in vendor termination.

Vendor Risk Assessment
Assess vendor risk based on: Data access, criticality to operations, financial stability, geographic location, regulatory compliance.

High-risk vendors require additional due diligence and monitoring. Annual risk reassessment for strategic vendors.

Payment Terms
Standard payment terms: Net 30 days. Early payment discounts negotiated when beneficial. Payment via ACH or wire transfer.

Vendors submit invoices with PO number. Payment processed after 3-way match (PO, receiving, invoice).

Vendor Compliance
Vendors must comply with our policies: Security, data protection, code of conduct, anti-corruption.

Vendor audits conducted for high-risk vendors. Non-compliance may result in contract termination.

Vendor Insurance Requirements
General liability insurance: $1M minimum. Professional liability: $1M for service providers. Workers compensation: As required by law.

Cyber liability: $2M for vendors with data access. Company named as additional insured on policies.

Vendor Data Protection
Vendors with access to company or customer data must sign data protection agreement (DPA).

DPA includes: Data handling requirements, security standards, breach notification, data retention, audit rights.

Vendor Offboarding
Terminating vendor relationships: Provide notice per contract terms. Ensure knowledge transfer and transition plan.

Revoke system access. Retrieve company property and data. Final invoice reconciliation. Update vendor status to inactive.

Vendor Diversity
We encourage vendor diversity including minority-owned, women-owned, veteran-owned, and small businesses.

Diversity considered in vendor selection alongside price, quality, and service. Report vendor diversity metrics annually.

Conflict of Interest
Employees must disclose relationships with vendors (family, financial interest, outside employment).

Disclosed conflicts reviewed by compliance. May require recusal from vendor selection or oversight.
""",

    "finance/reimbursement_steps.txt": """Employee Reimbursement Process

Reimbursement Eligibility
Employees reimbursed for approved business expenses paid with personal funds. Expenses must be reasonable, necessary, and properly documented.

Submit reimbursement requests within 30 days of expense. Late submissions may be denied.

Expense Report Submission
Submit expense reports through finance portal. Include: Date, vendor, amount, business purpose, attendees (if applicable).

Attach receipts for all expenses over $25. Categorize expenses correctly. Route to appropriate approver.

Required Documentation
Receipts must show: Date, vendor name, items purchased, amount paid. Credit card statements alone insufficient.

For meals: List attendees and business purpose. For mileage: Provide start/end locations and business purpose.

Approval Workflow
Expense reports route to manager for approval. Manager verifies business purpose and policy compliance.

Finance reviews for completeness and policy compliance. Approved reports processed for payment.

Reimbursement Timeline
Approved expense reports processed within 10 business days. Payment via direct deposit to payroll account.

Check payment available upon request but takes additional 3-5 days. International reimbursements may take longer.

Common Reimbursable Expenses
Business travel (flights, hotels, meals, transportation), client entertainment, office supplies, professional development, home office equipment (approved).

Mileage for business use of personal vehicle, mobile phone (if not provided by company), internet for remote workers.

Non-Reimbursable Expenses
Commuting costs, personal expenses, traffic violations, alcohol (except approved client entertainment), luxury items.

Late fees or interest charges, personal entertainment, gym memberships (except wellness program), personal travel.

Mileage Reimbursement
Personal vehicle use for business reimbursed at IRS standard rate. Submit mileage log with dates, destinations, business purpose, miles driven.

Only business miles reimbursed, not commuting. Use mapping tool to calculate distance. Round trip miles for there-and-back trips.

International Expense Reimbursement
Submit expenses in original currency. System converts using exchange rate on transaction date.

Keep currency exchange receipts. Credit card exchange rates acceptable. VAT refunds processed separately.

Corporate Card Reconciliation
Corporate card expenses require expense report even though company pays directly. Submit monthly reconciliation.

Categorize and document all charges. Personal charges must be reimbursed immediately. Missing receipts require explanation.

Rejected Expense Reports
Rejected reports returned with explanation. Common reasons: Missing receipts, policy violation, insufficient documentation, late submission.

Correct issues and resubmit. Contact finance with questions. Repeated violations may result in reimbursement privileges suspension.

Tax Implications
Some reimbursements may be taxable income (relocation, personal use of company property). Consult tax advisor for personal tax questions.

Company reports taxable reimbursements to tax authorities. Employees responsible for personal tax compliance.
""",

    "finance/audit_compliance.txt": """Audit and Compliance Requirements

Internal Audit Program
Internal audit conducts regular audits of financial controls, operational processes, and compliance. Audit schedule published annually.

Audits assess effectiveness of controls, identify risks, and recommend improvements. Audit findings tracked to resolution.

External Audit
Annual financial statement audit conducted by external auditors. Auditors review financial records, test controls, and issue opinion.

Cooperate fully with auditors. Provide requested documentation promptly. Address audit findings in timely manner.

Audit Preparation
Maintain organized financial records. Document processes and controls. Ensure policies are current and followed.

Conduct self-assessments before audits. Remediate known issues proactively. Assign audit coordinator for each department.

Audit Process
Auditors request documentation and conduct interviews. Provide accurate and complete information. Don't withhold or alter documents.

Auditors test samples of transactions. Explain processes and controls. Document verbal explanations in writing.

Audit Findings
Findings categorized by severity: Critical (immediate action required), High (significant risk), Medium (moderate risk), Low (best practice).

Management response required for all findings. Develop action plans with timelines. Track remediation progress.

Regulatory Compliance
Comply with applicable regulations: SOX (financial reporting), GDPR (data protection), industry-specific regulations.

Compliance team monitors regulatory changes. Training provided on compliance requirements. Report compliance concerns immediately.

Financial Controls
Segregation of duties: Different people authorize, record, and reconcile transactions. Prevents fraud and errors.

Approval authorities based on amount and transaction type. Regular reconciliations of accounts. Physical controls over assets.

Documentation Requirements
Maintain supporting documentation for all financial transactions. Retention periods vary by document type (typically 7 years).

Documents must be complete, accurate, and readily accessible. Electronic documents acceptable if properly stored and backed up.

Compliance Training
Annual compliance training required for all employees. Role-specific training for finance, procurement, and management.

Training covers: Code of conduct, anti-corruption, data protection, financial controls. Completion tracked and reported.

Whistleblower Policy
Report suspected fraud, waste, or abuse through ethics hotline (anonymous) or to compliance team.

All reports investigated promptly and confidentially. Retaliation against whistleblowers strictly prohibited.

Compliance Monitoring
Ongoing monitoring of compliance with policies and regulations. Automated controls where possible. Regular management reviews.

Compliance metrics reported to board quarterly. Trends analyzed to identify systemic issues.

Remediation and Corrective Action
Findings require corrective action plans with responsible parties and deadlines. Progress tracked and reported.

Verify effectiveness of corrective actions. Repeat findings escalated to senior management. Persistent non-compliance may result in disciplinary action.
""",

    "finance/finance_controls.txt": """Financial Controls and Procedures

Segregation of Duties
No single person controls all aspects of a financial transaction. Separate: Authorization, recording, custody, reconciliation.

Reduces fraud risk and errors. Small teams may require compensating controls like management review.

Authorization Controls
Transactions require appropriate authorization based on amount and type. Authorization matrix defines approval authorities.

Approvers verify business purpose, budget availability, and policy compliance. Document approvals in system.

Reconciliation Procedures
Bank reconciliations performed monthly within 10 days of month-end. Investigate and resolve discrepancies promptly.

Account reconciliations for all balance sheet accounts. Reconciler and reviewer must be different people.

Cash Handling
Minimize cash transactions - use electronic payments when possible. Cash receipts deposited daily.

Cash counts performed by two people. Cash access restricted to authorized personnel. Surprise cash counts conducted periodically.

Payment Controls
Payments require approved invoice, PO, and receiving confirmation (3-way match). Verify vendor banking details before first payment.

Dual approval for payments over $25000. Positive pay system prevents check fraud. ACH payments require dual authorization.

Revenue Recognition
Revenue recognized when earned and realizable per accounting standards. Document revenue recognition criteria for each revenue stream.

Review contracts for revenue recognition implications. Deferred revenue for advance payments.

Expense Accruals
Accrue expenses incurred but not yet invoiced. Review accruals monthly for accuracy. Reverse accruals when invoice received.

Estimate accruals based on contracts, POs, or historical patterns. Document accrual methodology.

Asset Management
Maintain fixed asset register with acquisition date, cost, location, and depreciation. Tag physical assets for tracking.

Annual physical inventory of assets. Investigate missing assets. Dispose of obsolete assets properly with approval.

Journal Entry Controls
Journal entries require supporting documentation and business purpose. Unusual or complex entries require additional review.

Restrict journal entry access to accounting personnel. Management reviews significant entries. Audit trail maintained.

Month-End Close Process
Standardized close process with checklist and deadlines. Close typically completes within 5 business days.

Review financial statements for reasonableness. Investigate unusual variances. Document significant estimates and judgments.

Financial Reporting
Monthly financial statements prepared for management. Quarterly reports for board. Annual audited statements.

Reports include: Income statement, balance sheet, cash flow, budget variance analysis. Narrative explanation of results.

Internal Control Testing
Periodic testing of key controls. Document control procedures. Test samples of transactions.

Identify control deficiencies and remediate. Report significant deficiencies to audit committee.
""",

    "security/soc_alert_handling.txt": """Security Operations Center Alert Handling

Alert Triage
SOC monitors security alerts 24/7. Alerts triaged by severity: Critical (immediate threat), High (potential threat), Medium (suspicious), Low (informational).

Triage within: Critical - 15 minutes, High - 1 hour, Medium - 4 hours, Low - next business day.

Alert Sources
Alerts from: SIEM, IDS/IPS, endpoint protection, firewall, email security, cloud security, threat intelligence feeds.

Automated correlation reduces false positives. Machine learning identifies anomalous patterns.

Initial Assessment
Analyst reviews alert details: Source, destination, user, time, indicators of compromise (IOCs).

Check if alert is false positive based on known patterns. Verify if activity is authorized or expected.

Investigation Procedures
Gather additional context: User activity, system logs, network traffic, related alerts.

Check threat intelligence for known malicious IPs, domains, or file hashes. Determine if incident or false positive.

Escalation Criteria
Escalate to senior analyst if: Confirmed malicious activity, data exfiltration suspected, multiple systems affected, advanced persistent threat (APT) indicators.

Critical incidents escalated to incident commander and CISO. Stakeholders notified per communication plan.

Containment Actions
Isolate affected systems from network if active threat. Disable compromised accounts. Block malicious IPs/domains at firewall.

Preserve evidence for forensic analysis. Don't alert attacker that they've been detected if ongoing investigation.

Documentation Requirements
Document all investigation steps, findings, and actions taken. Use standardized incident ticket format.

Include: Timeline, affected systems, IOCs, root cause, containment actions, remediation steps. Attach relevant logs and screenshots.

False Positive Handling
Document reason for false positive determination. Tune detection rules to reduce future false positives.

Track false positive rate by alert type. High false positive rates indicate need for rule refinement.

Threat Hunting
Proactive searching for threats not detected by automated tools. Use threat intelligence and attack patterns.

Hunt for: Lateral movement, privilege escalation, persistence mechanisms, data staging. Document findings and improve detections.

Alert Metrics
Track: Alert volume, false positive rate, mean time to detect (MTTD), mean time to respond (MTTR), escalation rate.

Review metrics weekly. Identify trends and improvement opportunities. Report to management monthly.

Shift Handoff
Handoff between shifts includes: Active incidents, ongoing investigations, system issues, upcoming maintenance.

Use standardized handoff template. Incoming shift reviews handoff notes and asks clarifying questions.

Continuous Improvement
Post-incident reviews identify lessons learned. Update runbooks and procedures. Improve detection rules.

Share knowledge across team. Training on new threats and techniques. Participate in threat intelligence community.
""",

    "security/threat_intelligence_guide.txt": """Threat Intelligence Program

Threat Intelligence Overview
Threat intelligence provides context about threats, adversaries, and attack techniques. Enables proactive defense and informed decision-making.

Sources: Commercial feeds, open source intelligence (OSINT), information sharing groups, internal telemetry.

Intelligence Collection
Collect indicators of compromise (IOCs): Malicious IPs, domains, file hashes, URLs. Tactics, techniques, and procedures (TTPs) of threat actors.

Vulnerability intelligence: New vulnerabilities, exploits, patches. Industry-specific threats and trends.

Intelligence Analysis
Analyze intelligence for relevance to our environment. Prioritize based on likelihood and potential impact.

Correlate intelligence with internal security data. Identify gaps in defenses. Provide actionable recommendations.

Threat Actor Profiling
Track known threat actors targeting our industry. Understand their motivations, capabilities, and TTPs.

Attribution helps predict future attacks and tailor defenses. Share profiles with SOC and incident response teams.

Indicator Management
Ingest IOCs into security tools (SIEM, firewall, endpoint protection). Automate blocking of known malicious indicators.

Regularly update and expire old indicators. Track indicator effectiveness and false positive rates.

Threat Intelligence Sharing
Participate in industry information sharing groups (ISACs). Share anonymized threat data with community.

Receive early warnings of threats targeting our sector. Collaborate on threat research and mitigation strategies.

Intelligence Dissemination
Distribute intelligence to relevant stakeholders: SOC, incident response, IT, management.

Tailor intelligence to audience: Technical details for SOC, strategic overview for executives. Use standardized formats (STIX, TAXII).

Threat Modeling
Identify likely threats to our assets and operations. Model attack scenarios and potential impacts.

Use threat intelligence to validate and update threat models. Prioritize security investments based on threat landscape.

Vulnerability Intelligence
Monitor vulnerability disclosures relevant to our technology stack. Assess exploitability and potential impact.

Prioritize patching based on threat intelligence. Track if vulnerabilities are being actively exploited.

Dark Web Monitoring
Monitor dark web for mentions of company, leaked credentials, or planned attacks.

Track sale of access to our systems or data. Alert relevant teams to take protective actions.

Threat Intelligence Platforms
Use threat intelligence platform (TIP) to aggregate, analyze, and disseminate intelligence.

Integrate TIP with security tools for automated response. Track intelligence workflow and effectiveness.

Metrics and Reporting
Track: Intelligence sources used, IOCs ingested, threats detected, incidents prevented.

Report threat landscape trends to management quarterly. Demonstrate value of threat intelligence program.
""",

    "security/data_classification.txt": """Data Classification and Handling

Classification Levels
Public: Information intended for public disclosure. No confidentiality required.

Internal: Information for internal use. Not for public disclosure but low risk if exposed.

Confidential: Sensitive business information. Unauthorized disclosure could harm company.

Restricted: Highly sensitive data. Unauthorized disclosure could cause severe harm. Includes personal data, financial data, trade secrets.

Classification Criteria
Consider: Sensitivity, regulatory requirements, business impact of disclosure, privacy implications.

When in doubt, classify at higher level. Data owner determines classification. Review classification periodically.

Handling Requirements - Public
No special handling required. Can be shared freely. Store on any company system.

Examples: Marketing materials, press releases, public website content, published reports.

Handling Requirements - Internal
Share only with employees and authorized contractors. Don't share on public websites or social media.

Store on company systems with access controls. Email to company addresses only.

Examples: Internal policies, org charts, project plans, internal communications.

Handling Requirements - Confidential
Share only with employees who need to know. Require NDA for external sharing.

Encrypt in transit and at rest. Store on approved systems with strong access controls. Don't store on personal devices.

Examples: Financial results (pre-release), customer lists, contracts, strategic plans, employee data.

Handling Requirements - Restricted
Strict need-to-know access. Require executive approval for external sharing.

Strong encryption required. Multi-factor authentication for access. Detailed access logging and monitoring.

Examples: Customer personal data, payment card data, trade secrets, M&A information, security vulnerabilities.

Data Labeling
Label documents and emails with classification level. Use classification markings in headers/footers.

Email subject lines should indicate classification for Confidential and Restricted data.

Data Storage
Public/Internal: Standard company storage systems.

Confidential: Encrypted storage with access controls. Approved cloud storage with encryption.

Restricted: Encrypted storage with strict access controls. May require on-premises storage for some data types.

Data Transmission
Public/Internal: Standard email and file sharing.

Confidential: Encrypted email or secure file sharing. VPN for remote access.

Restricted: Encrypted email with additional authentication. Secure file transfer protocols. No transmission to personal email.

Data Disposal
Public/Internal: Standard deletion.

Confidential: Secure deletion ensuring data cannot be recovered.

Restricted: Cryptographic erasure or physical destruction. Certificate of destruction for physical media.

Third-Party Data Sharing
Assess third-party security before sharing Confidential or Restricted data. Require data protection agreement (DPA).

Specify permitted uses, security requirements, and data retention. Audit third-party compliance.

Data Classification Training
All employees complete annual data classification training. Understand classification levels and handling requirements.

Data owners receive additional training on classification decisions. Regular reminders and updates.

Compliance and Audits
Audit data handling practices regularly. Verify compliance with classification requirements.

Report violations to security team. Remediate issues promptly. Track metrics on classification compliance.
""",

    "security/access_control_standards.txt": """Access Control Standards

Access Control Principles
Least privilege: Users have minimum access needed for their role. Need-to-know: Access granted only for legitimate business need.

Separation of duties: No single user has excessive privileges. Regular access reviews ensure appropriate access.

User Account Management
Unique user accounts for each person. No shared accounts except approved service accounts.

Account creation requires manager approval. Access provisioned based on role and department. Accounts disabled immediately upon termination.

Authentication Requirements
Strong passwords required (12+ characters, complexity). Multi-factor authentication (MFA) mandatory for all systems.

Biometric authentication encouraged where available. Single sign-on (SSO) for integrated systems.

Authorization Levels
Read-only: View data but cannot modify. User: Standard access for role. Power user: Additional capabilities for advanced users.

Administrator: Full system control. Granted sparingly with approval. Privileged access monitored closely.

Role-Based Access Control
Access assigned based on job role. Standard roles defined for common positions.

Custom roles for unique requirements. Role changes trigger access review and adjustment.

Access Request Process
Submit access requests through IT portal. Include: System, access level, business justification.

Manager approval required. Additional approval for privileged access. Access provisioned within 1 business day.

Access Reviews
Quarterly access reviews by managers. Verify each user's access is still appropriate.

Remove unnecessary access. Document review completion. Audit tracks review compliance.

Privileged Access Management
Privileged accounts (admin, root) require additional controls. Just-in-time access: Elevated privileges granted temporarily when needed.

Privileged sessions recorded. Regular audits of privileged account usage.

Service Accounts
Service accounts for automated processes and applications. Strong passwords (20+ characters). Stored in password manager.

Access restricted to authorized personnel. Regular password rotation. Document service account purpose and owner.

Remote Access Control
VPN required for remote access to company resources. MFA enforced for VPN connections.

Remote desktop access restricted to approved users. Session timeouts for inactive connections.

Physical Access Control
Badge access to office facilities. Visitor sign-in and escort required.

Server room access restricted to authorized IT personnel. Access logs reviewed monthly.

Access Termination
Immediate access revocation upon termination. Disable accounts, revoke VPN, collect badges and devices.

Transfer data ownership before departure. Document access removal completion.

Guest and Contractor Access
Temporary accounts for contractors and guests. Limited access based on need.

Sponsor responsible for guest access. Access expires automatically. Regular review of active guest accounts.

Access Monitoring
Log all access to sensitive systems and data. Monitor for unusual access patterns.

Alert on: After-hours access, failed login attempts, privilege escalation, access from unusual locations.

Access Violations
Report access violations to security team. Investigate unauthorized access attempts.

Violations may result in disciplinary action. Repeated violations may lead to termination.

Compliance Requirements
Access controls comply with regulatory requirements (SOX, GDPR, HIPAA where applicable).

Document access control procedures. Demonstrate compliance during audits.
""",

    "security/forensic_procedure.txt": """Digital Forensics Procedure

Forensic Investigation Triggers
Forensic investigation initiated for: Suspected data breach, insider threat, policy violation, legal hold, malware incident.

Security team determines if forensics needed. Legal counsel consulted for investigations with legal implications.

Evidence Preservation
Preserve evidence immediately upon incident detection. Don't alter or access affected systems unnecessarily.

Document chain of custody for all evidence. Use write-blockers for disk imaging. Maintain evidence integrity.

Forensic Imaging
Create bit-for-bit copies of affected systems. Use forensically sound tools (FTK Imager, dd).

Verify image integrity with cryptographic hashes (SHA-256). Store original evidence securely. Work only on copies.

Evidence Collection
Collect: Disk images, memory dumps, log files, network captures, email, documents.

Document: System configuration, running processes, network connections, user accounts, timestamps.

Maintain detailed notes of all collection activities.

Chain of Custody
Document who collected evidence, when, where, and how. Track all evidence transfers.

Store evidence in secure location with restricted access. Log all access to evidence.

Maintain chain of custody documentation for legal proceedings.

Analysis Methodology
Systematic analysis of collected evidence. Timeline reconstruction of events.

Identify: What happened, when, how, who was involved, what data was affected.

Use forensic tools: EnCase, Autopsy, Volatility, Wireshark. Document all analysis steps and findings.

Memory Analysis
Analyze RAM dumps for: Running processes, network connections, loaded drivers, encryption keys.

Memory analysis reveals information not available from disk. Volatile data lost if system powered off.

Network Forensics
Analyze network traffic captures. Identify: Communication with malicious IPs, data exfiltration, lateral movement.

Reconstruct network sessions. Extract files transferred. Identify command and control traffic.

Log Analysis
Correlate logs from multiple sources: System logs, application logs, security logs, network logs.

Identify: Authentication events, file access, process execution, network connections.

Timeline analysis reveals sequence of events.

Malware Analysis
Analyze suspicious files in isolated sandbox environment. Identify: Malware capabilities, indicators of compromise, command and control infrastructure.

Static analysis: File properties, strings, imports. Dynamic analysis: Behavior observation, network activity.

Reporting Findings
Comprehensive forensic report documenting: Investigation scope, methodology, findings, evidence, conclusions.

Include: Timeline of events, technical details, business impact, recommendations.

Report suitable for technical and non-technical audiences. May be used in legal proceedings.

Legal Considerations
Consult legal counsel before investigation. Understand legal requirements and constraints.

Maintain evidence integrity for admissibility. Follow proper procedures for chain of custody.

Privacy considerations for employee data. Comply with data protection regulations.

Expert Testimony
Forensic investigators may be called as expert witnesses. Maintain detailed documentation to support testimony.

Be prepared to explain methodology and findings. Maintain professional certifications and training.

Forensic Tools and Training
Use industry-standard forensic tools. Maintain tool licenses and updates.

Forensic team maintains certifications: GCFE, EnCE, CHFI. Regular training on new techniques and tools.

Evidence Retention
Retain evidence per legal and regulatory requirements. Typically 7 years for legal matters.

Secure storage with restricted access. Document evidence disposal when retention period expires.
""",

    "security/password_rotation_standards.txt": """Password Rotation and Management Standards

Password Rotation Policy
User passwords expire every 90 days. System prompts password change 7 days before expiration.

Service account passwords rotated annually. Privileged account passwords rotated every 60 days.

Immediate rotation required if compromise suspected.

Password History
Cannot reuse last 10 passwords. System enforces password history.

Prevents cycling through small set of passwords. Encourages use of password manager for unique passwords.

Password Complexity
Minimum 12 characters. Must include: Uppercase, lowercase, numbers, special characters.

No dictionary words, personal information, or common patterns. System validates complexity on password change.

Password Manager Requirement
All employees must use company password manager (1Password). Generates strong random passwords.

Stores passwords securely with encryption. Syncs across devices. Enables unique passwords for each account.

Emergency Password Changes
Change passwords immediately if: Account compromised, password shared, employee terminated with shared knowledge.

Security team can force password reset for all users if widespread compromise suspected.

Service Account Password Rotation
Service accounts require 20+ character randomly generated passwords. Stored in password manager with restricted access.

Rotation coordinated with application owners. Test applications after password change. Document rotation completion.

Privileged Account Passwords
Administrator and root passwords require extra security. Stored in privileged access management (PAM) system.

Check-out/check-in process for privileged password use. Session recording for accountability.

Password Reset Process
Self-service password reset via IT portal. Verify identity with security questions or MFA.

Helpdesk can reset with identity verification. Temporary password must be changed on first login.

Password Sharing Prohibition
Never share passwords. Each person must have unique account.

Use password manager's secure sharing for legitimate sharing needs (team accounts).

Sharing passwords violates policy and may result in disciplinary action.

Password Storage
Store passwords only in approved password manager. Never in: Plain text files, spreadsheets, sticky notes, browser (except password manager extension).

Encrypt any documents containing passwords. Limit access to password repositories.

Third-Party Account Passwords
Use SSO for third-party services when available. For services without SSO, follow same password standards.

Store third-party passwords in password manager. Enable MFA on third-party accounts.

Password Audits
IT conducts periodic password audits. Identifies: Weak passwords, expired passwords, shared accounts, password reuse.

Users notified of password issues. Compliance required within 48 hours.

Compromised Password Response
If password found in breach database, force immediate reset. Notify user of compromise.

Check for unauthorized account activity. Monitor account for suspicious behavior.

Password Training
Annual security training includes password best practices. New employees receive password training during onboarding.

Regular reminders about password security. Phishing simulations test password protection.

Password Exceptions
Exceptions to rotation policy require security team approval. Documented justification required.

Compensating controls may be required (additional monitoring, restricted access).

Exceptions reviewed annually.
""",

    "security/risk_assessment_methodology.txt": """Risk Assessment Methodology

Risk Assessment Overview
Systematic process to identify, analyze, and evaluate information security risks.

Conducted annually and when significant changes occur. Informs security strategy and resource allocation.

Risk Identification
Identify threats: Cyberattacks, insider threats, natural disasters, system failures, human error.

Identify vulnerabilities: Unpatched systems, weak configurations, inadequate controls, process gaps.

Identify assets: Data, systems, applications, infrastructure, people.

Threat Analysis
Analyze threat sources: External attackers, insiders, competitors, nation-states, hacktivists.

Assess threat capabilities and motivations. Consider threat intelligence and industry trends.

Evaluate likelihood of threat exploitation.

Vulnerability Assessment
Technical vulnerability scanning of systems and applications. Configuration reviews against security baselines.

Penetration testing to identify exploitable vulnerabilities. Process and control reviews.

Assess vulnerability severity and exploitability.

Asset Valuation
Determine asset value based on: Confidentiality, integrity, availability requirements.

Consider: Business impact of loss, regulatory requirements, replacement cost, reputation impact.

Classify assets by criticality to operations.

Risk Analysis
Combine threat likelihood and vulnerability severity. Assess potential impact to confidentiality, integrity, availability.

Calculate risk level: Risk = Likelihood × Impact.

Consider existing controls and their effectiveness.

Risk Evaluation
Compare calculated risks against risk appetite. Prioritize risks for treatment.

High risks require immediate attention. Medium risks addressed in planned timeframe. Low risks may be accepted.

Risk Treatment Options
Mitigate: Implement controls to reduce risk. Accept: Acknowledge risk and accept consequences (for low risks).

Transfer: Use insurance or outsourcing to transfer risk. Avoid: Eliminate activity causing risk.

Document risk treatment decisions and rationale.

Control Selection
Select controls based on: Risk level, cost-effectiveness, feasibility, regulatory requirements.

Consider: Technical controls (firewalls, encryption), administrative controls (policies, training), physical controls (locks, cameras).

Implement defense in depth with multiple control layers.

Risk Treatment Plan
Document planned risk treatments with: Responsible party, timeline, resources required, success criteria.

Track implementation progress. Verify control effectiveness after implementation.

Residual Risk Assessment
Assess remaining risk after controls implemented. Determine if residual risk is acceptable.

Additional controls may be needed if residual risk too high. Document accepted residual risks.

Risk Monitoring
Continuously monitor risk landscape. Track new threats and vulnerabilities.

Monitor control effectiveness. Conduct periodic risk reassessments.

Update risk register with changes.

Risk Reporting
Report risk assessment results to management and board. Highlight: Top risks, risk trends, treatment progress.

Provide risk-based recommendations for security investments.

Quarterly risk updates to leadership.

Risk Register
Maintain centralized risk register documenting: Identified risks, risk ratings, treatment plans, owners, status.

Risk register is living document updated regularly. Used for risk tracking and reporting.

Compliance Integration
Integrate compliance requirements into risk assessment. Ensure controls address regulatory obligations.

Document compliance status. Report compliance risks to management.
""",

    "security/incident_severity_matrix.txt": """Security Incident Severity Matrix

Severity Levels Overview
Incidents classified by severity to ensure appropriate response. Severity based on: Impact, scope, data sensitivity, business criticality.

P1 (Critical), P2 (High), P3 (Medium), P4 (Low). Severity determines response time and escalation.

P1 - Critical Incidents
Definition: Severe impact to business operations or data. Active data breach or ransomware. Customer-facing systems down. Widespread system compromise.

Response Time: 15 minutes. Escalation: Immediate to incident commander and CISO. Notification: Executive team, legal, PR.

Examples: Active data exfiltration, ransomware encryption, complete system outage, confirmed APT.

P2 - High Incidents
Definition: Significant impact to operations or data. Potential data breach. Important systems impaired. Multiple systems compromised.

Response Time: 1 hour. Escalation: Senior security analyst and manager. Notification: Department heads, IT leadership.

Examples: Malware infection, unauthorized access to sensitive data, DDoS attack, significant vulnerability exploitation.

P3 - Medium Incidents
Definition: Moderate impact. Single system compromised. Minor data exposure. Degraded performance.

Response Time: 4 hours. Escalation: Security analyst. Notification: Affected department, IT team.

Examples: Phishing attempt, policy violation, minor malware, unsuccessful attack attempt, suspicious activity.

P4 - Low Incidents
Definition: Minimal impact. Informational alerts. Potential security concerns. No immediate threat.

Response Time: Next business day. Escalation: None unless pattern emerges. Notification: Security team only.

Examples: Failed login attempts, low-risk vulnerability, security awareness issue, minor policy violation.

Impact Assessment Factors
Confidentiality: Data exposure or theft. Integrity: Data modification or corruption. Availability: System or service disruption.

Scope: Number of systems, users, or customers affected. Duration: Length of impact or exposure.

Data Sensitivity: Classification level of affected data.

Business Impact Criteria
Revenue impact: Lost sales, transaction processing disruption. Reputation: Customer trust, brand damage, media attention.

Regulatory: Compliance violations, reporting requirements. Legal: Potential lawsuits, contractual breaches.

Operational: Productivity loss, recovery costs.

Severity Escalation
Incidents may be escalated to higher severity as investigation reveals greater impact.

Escalation triggers: Broader scope than initially assessed, sensitive data involved, prolonged duration, regulatory implications.

Document escalation rationale.

Severity Downgrade
Incidents may be downgraded if impact less severe than initially assessed.

Downgrade only after thorough investigation confirms lower impact. Document downgrade justification.

Maintain audit trail of severity changes.

Response Time SLAs
P1: Acknowledge 15 min, Initial assessment 30 min, Containment 2 hours.

P2: Acknowledge 1 hour, Initial assessment 2 hours, Containment 8 hours.

P3: Acknowledge 4 hours, Initial assessment 8 hours, Containment 24 hours.

P4: Acknowledge next business day, Assessment 3 days, Resolution 5 days.

Communication Requirements
P1: Hourly updates to stakeholders. Status page updates. Executive briefings.

P2: Updates every 4 hours. Stakeholder notifications. Management briefings.

P3: Daily updates. Affected parties notified. Standard reporting.

P4: Update on resolution. Documented in ticket. Monthly summary reporting.

Severity-Based Resources
P1: Full incident response team, external experts if needed, dedicated resources.

P2: Senior analysts, manager involvement, additional resources as needed.

P3: Assigned analyst, standard resources.

P4: Analyst as available, standard tools.

Post-Incident Review Requirements
P1/P2: Mandatory post-incident review within 48 hours. Root cause analysis. Lessons learned. Action items.

P3: Review if recurring or significant learning opportunity.

P4: Documented in ticket, no formal review unless pattern identified.
""",

    "general/code_of_conduct.txt": """Code of Conduct

Our Values
Integrity: Act honestly and ethically in all situations. Respect: Treat everyone with dignity and respect.

Excellence: Strive for high quality in everything we do. Collaboration: Work together to achieve common goals.

Innovation: Embrace new ideas and continuous improvement.

Professional Behavior
Conduct yourself professionally in all business interactions. Represent the company positively.

Be punctual for meetings and commitments. Communicate clearly and respectfully.

Take responsibility for your actions and decisions.

Respect and Inclusion
We are committed to diverse and inclusive workplace. Respect differences in background, perspective, and experience.

No discrimination based on race, gender, religion, age, disability, sexual orientation, or other protected characteristics.

Create welcoming environment where everyone can contribute and succeed.

Harassment Prevention
Zero tolerance for harassment of any kind. Harassment includes: Unwelcome conduct, offensive comments, intimidation, bullying.

Sexual harassment strictly prohibited. Report harassment immediately to HR or ethics hotline.

Workplace Safety
Maintain safe work environment. Follow safety procedures and guidelines.

Report safety hazards immediately. Don't work under influence of alcohol or drugs.

Emergency procedures posted in all locations. Participate in safety drills.

Confidentiality
Protect confidential company information. Don't disclose to unauthorized parties.

Includes: Trade secrets, financial data, customer information, strategic plans, employee data.

Confidentiality obligations continue after employment ends.

Conflicts of Interest
Avoid situations where personal interests conflict with company interests.

Disclose: Outside employment, financial interests in competitors/vendors, personal relationships with colleagues in reporting line.

When in doubt, disclose to manager or HR.

Gifts and Entertainment
Don't accept gifts or entertainment that could influence business decisions.

Nominal gifts (under $50) acceptable. Anything more requires disclosure and approval.

Never offer bribes or improper payments to customers, vendors, or officials.

Company Resources
Use company resources responsibly and primarily for business purposes.

Includes: Equipment, supplies, internet, email, software, facilities.

Limited personal use acceptable if doesn't interfere with work.

Social Media
You may mention employment on social media. Make clear views are your own, not company's.

Don't share confidential information. Don't disparage company, colleagues, or customers.

Represent company professionally online.

Reporting Violations
Report suspected violations of this code to: Manager, HR, compliance team, or ethics hotline (anonymous).

All reports investigated promptly and confidentially. No retaliation for good faith reports.

Compliance Responsibility
Everyone responsible for understanding and following this code.

Violations may result in disciplinary action up to termination.

Managers have additional responsibility to model ethical behavior and address concerns.

Questions and Guidance
If unsure about appropriate action, ask: Manager, HR, compliance team.

Better to ask than risk violation. Resources available to help you make ethical decisions.

Annual Acknowledgment
All employees must acknowledge reading and understanding code of conduct annually.

Acknowledgment tracked in HR system. Completion required for continued employment.
""",

    "general/company_faq.txt": """Company Frequently Asked Questions

About Our Company
Q: What does our company do?
A: We develop innovative software products that help businesses improve productivity and collaboration. Our flagship products serve over 10,000 customers worldwide.

Q: When was the company founded?
A: Founded in 2015 by a team of engineers passionate about solving real business problems with technology.

Q: Where are we located?
A: Headquarters in San Francisco with offices in New York, London, and Singapore. We also have remote employees across 15 countries.

Working Here
Q: What's the company culture like?
A: We value innovation, collaboration, and work-life balance. Flat hierarchy, open communication, and continuous learning are core to our culture.

Q: What are the working hours?
A: Flexible schedule with core hours 10 AM - 4 PM local time. We trust you to manage your time and deliver results.

Q: Is remote work available?
A: Yes, remote work is fully supported. Many employees work remotely full-time. Hybrid arrangements also available.

Benefits and Compensation
Q: What benefits do you offer?
A: Comprehensive health insurance, 401(k) with matching, stock options, generous PTO, parental leave, professional development budget, home office stipend.

Q: When do benefits start?
A: Health insurance starts on your first day. 401(k) eligibility after 3 months. Stock options vest over 4 years.

Q: How often are performance reviews?
A: Formal reviews twice annually (June and December). Continuous feedback encouraged throughout the year.

Career Development
Q: Are there opportunities for advancement?
A: Yes, we support career growth through internal mobility, promotions, and development programs. Both individual contributor and management tracks available.

Q: What training is available?
A: $2000 annual learning budget per employee. Access to online learning platforms. Internal training programs. Conference attendance.

Q: Can I change departments?
A: Internal mobility encouraged. Current employees given priority for open positions. Discuss career interests with your manager.

Technology and Tools
Q: What equipment is provided?
A: Laptop (Mac or PC), monitor, keyboard, mouse, necessary software. Additional equipment based on role needs.

Q: What collaboration tools do we use?
A: Slack for messaging, Zoom for video, Google Workspace for documents, Jira for project management, GitHub for code.

Q: Can I use my own devices?
A: Personal devices can access email and approved cloud services with MDM profile. Company devices provided for primary work.

Time Off
Q: How much vacation do I get?
A: 20 days annual leave plus 10 sick days. Public holidays observed. Parental leave available.

Q: How do I request time off?
A: Submit through HR portal at least 2 weeks in advance. Manager approval required. Emergency leave can be requested via email.

Q: Can I carry over unused vacation?
A: Up to 5 days can be carried to next year. Excess days forfeited unless exceptional circumstances.

Getting Help
Q: Who do I contact for IT issues?
A: IT helpdesk via portal, email (helpdesk@company.com), or phone. Available 24/7 for critical issues.

Q: Who handles HR questions?
A: Your HR business partner or hr@company.com. HR available Monday-Friday 9 AM - 5 PM.

Q: What if I have a complaint?
A: Talk to your manager, HR, or use anonymous ethics hotline. All concerns taken seriously and investigated.

Company Policies
Q: Where can I find company policies?
A: Employee portal has all policies and handbooks. Key policies covered in onboarding. Annual policy acknowledgment required.

Q: What's the dress code?
A: Business casual in office. Dress appropriately for client meetings. Remote workers dress professionally for video calls.

Q: Can I work from another location temporarily?
A: Yes, with manager approval. Notify HR for stays over 2 weeks. Permanent relocation requires HR approval.
""",

    "general/communication_guidelines.txt": """Communication Guidelines

Communication Principles
Be clear and concise. Respect others' time. Choose appropriate communication channel.

Respond promptly during work hours. Be professional and respectful. Consider cultural and time zone differences.

Email Best Practices
Use clear, descriptive subject lines. Keep emails focused on one topic. Use bullet points for readability.

Reply within 24 hours during work week. Use "Reply All" judiciously. Proofread before sending.

CC only those who need to know. BCC for large distribution lists to protect privacy.

Slack Usage
Use channels for team discussions. Direct messages for private conversations. Threads to keep conversations organized.

@mention specific people when you need their attention. Don't @channel unless urgent and relevant to everyone.

Update status when away. Use Do Not Disturb outside work hours. Emoji reactions for quick acknowledgments.

Video Meetings
Test audio/video before important meetings. Join on time. Mute when not speaking.

Use video when possible for better engagement. Professional background or virtual background.

Minimize distractions. Take notes. Share screen when presenting.

Meeting Etiquette
Send agenda in advance. Start and end on time. Stay focused on agenda topics.

One person speaks at a time. Encourage participation from all attendees. Summarize action items and owners.

Send meeting notes and action items after meeting.

Phone Communication
Answer professionally with name and greeting. Speak clearly. Take notes during calls.

Return voicemails within 24 hours. Use speakerphone only in private spaces.

Schedule calls in advance when possible. Confirm time zones for calls with remote colleagues.

Written Communication
Use professional tone. Avoid jargon and acronyms unless audience familiar.

Proofread for grammar and spelling. Format for readability with paragraphs and spacing.

Be mindful of tone - written communication can be misinterpreted.

Cross-Cultural Communication
Be aware of cultural differences in communication styles. Some cultures more direct, others more indirect.

Avoid idioms and slang that may not translate. Be patient with non-native speakers.

Clarify understanding rather than assuming. Show respect for different perspectives.

Time Zone Considerations
Check colleagues' time zones before scheduling meetings. Use time zone converter tools.

Avoid scheduling meetings outside others' work hours when possible. Record meetings for those who can't attend live.

Clearly state time zone in meeting invites (e.g., "2 PM EST").

Urgent Communication
For urgent matters, use phone or Slack direct message. Mark emails as urgent only when truly urgent.

Follow up if no response within reasonable time. Escalate to manager if critical and no response.

Define what constitutes urgent for your team.

Feedback and Difficult Conversations
Give feedback promptly and privately. Be specific and constructive. Focus on behavior, not person.

Listen actively. Seek to understand before being understood. Assume positive intent.

Follow up in writing to document discussion and agreements.

Communication Channels
Email: Formal communication, external communication, documentation, non-urgent matters.

Slack: Quick questions, team coordination, informal communication, real-time collaboration.

Video: Complex discussions, team meetings, presentations, relationship building.

Phone: Urgent matters, sensitive topics, when tone is important.

Documentation
Document important decisions and agreements. Use shared documents for collaboration.

Keep documentation current. Make documentation easily accessible. Use clear naming conventions.

Version control for important documents.

Communication Accessibility
Provide captions for videos. Use alt text for images. Ensure documents are screen-reader friendly.

Offer multiple communication options. Be patient with different communication needs.

Ask about communication preferences.
""",

    "general/office_hours.txt": """Office Hours and Schedules

Standard Office Hours
Office locations open Monday-Friday, 8 AM - 6 PM local time. Core hours: 10 AM - 4 PM when all employees expected to be available.

Flexible schedule outside core hours. Work-life balance encouraged.

Flexible Work Arrangements
Flexible start/end times with manager approval. Compressed work weeks (e.g., 4x10) may be available.

Part-time arrangements considered case-by-case. Discuss flexibility needs with your manager.

Remote Work Schedule
Remote employees follow same core hours requirement. Maintain regular schedule for team coordination.

Communicate schedule to team. Update calendar with working hours. Be responsive during core hours.

Time Tracking
Non-exempt employees track hours worked. Submit timesheets weekly by Friday end of day.

Exempt employees not required to track hours but expected to work full-time schedule.

Overtime for non-exempt employees requires pre-approval.

Breaks and Lunch
Take regular breaks throughout day. Lunch break typically 30-60 minutes.

Step away from desk. Breaks improve productivity and wellbeing.

No specific break schedule required - manage your time.

After-Hours Work
Avoid working excessive hours. Disconnect after work day. Respect others' off-hours.

After-hours work occasionally necessary but shouldn't be routine. Discuss workload concerns with manager.

On-call rotations compensated with time off or additional pay.

Holidays
Company observes national holidays. Holiday schedule published annually.

Office closed on holidays. Holiday pay for eligible employees.

If holiday falls on weekend, following Monday observed.

Paid Time Off
Use PTO for vacation, personal days, appointments. Submit requests in advance.

Minimum 2-week notice for week-long vacations. Manager approval required.

Encourage taking regular time off for wellbeing.

Sick Leave
Stay home when sick. Don't come to office with contagious illness.

Notify manager as soon as possible. No medical certificate needed for short absences.

Focus on recovery. Work can wait.

Weather and Emergencies
Office may close for severe weather or emergencies. Notification via email and Slack.

Remote work available during office closures. Safety is priority.

Use judgment about commuting in bad weather.

Meeting-Free Time
Some teams designate meeting-free times (e.g., Friday afternoons) for focused work.

Respect team norms about meeting schedules. Avoid scheduling meetings during lunch hours.

Block focus time on your calendar.

Global Team Coordination
Coordinate across time zones for global teams. Rotate meeting times to share inconvenience.

Record meetings for those who can't attend live. Use asynchronous communication when possible.

Be mindful of colleagues' local times.

Schedule Changes
Communicate schedule changes to team. Update calendar and Slack status.

Notify manager of regular schedule changes. Temporary changes (appointments, etc.) just need calendar update.

Consistency helps team coordination.
""",

    "general/emergency_contacts.txt": """Emergency Contacts and Procedures

Emergency Services
Life-threatening emergency: Call 911 (US) or local emergency number immediately.

Medical emergency, fire, or immediate danger: Evacuate if safe, then call emergency services.

Company security: Available 24/7 for facility emergencies.

Office Emergency Contacts
San Francisco Office: Security (415) 555-0100, Facilities (415) 555-0101

New York Office: Security (212) 555-0200, Facilities (212) 555-0201

London Office: Security +44 20 5550 0300, Facilities +44 20 5550 0301

Singapore Office: Security +65 5550 0400, Facilities +65 5550 0401

IT Emergency Support
IT Helpdesk 24/7: (888) 555-HELP or helpdesk@company.com

Critical system outage: Call helpdesk and mark as P1 incident

Security incidents: security@company.com or (888) 555-SEC1

HR Emergency Contacts
HR Main Line: (888) 555-HR00 (Monday-Friday 9 AM - 5 PM)

After-hours HR emergency: (888) 555-HR24

Employee Assistance Program (EAP): (800) 555-EAP1 (24/7 confidential counseling)

Management Emergency Contacts
Your direct manager: Contact info in employee portal

Department head: Contact info in employee portal

Executive on-call: (888) 555-EXEC (for critical business emergencies)

Medical Emergencies
Call 911 or local emergency services immediately. Notify office security or manager.

First aid kits located in break rooms. AED devices in main lobbies.

Trained first responders identified with badges in offices.

Fire Emergency
Activate fire alarm. Evacuate immediately using nearest exit.

Don't use elevators. Proceed to designated assembly point.

Don't re-enter building until cleared by fire department.

Severe Weather
Monitor weather alerts. Follow local emergency management guidance.

Office may close for severe weather. Notification via email and Slack.

Remote work available during weather emergencies.

Active Threat
Run: Evacuate if safe route available. Hide: Lock doors, turn off lights, silence phones.

Fight: As last resort, use any means to defend yourself.

Call 911 when safe. Notify company security.

Workplace Violence
Report threats or concerning behavior to HR and security immediately.

Don't confront threatening individuals. Remove yourself from situation.

Company has zero tolerance for workplace violence.

Evacuation Procedures
Know evacuation routes and assembly points. Assist visitors and colleagues with disabilities.

Don't stop to collect belongings. Account for team members at assembly point.

Wait for all-clear before returning to building.

Business Continuity
Critical systems have backup and recovery procedures. IT maintains disaster recovery plans.

Remote work capabilities for business continuity. Essential personnel identified for each function.

Regular testing of continuity plans.

Personal Emergency
Notify manager if personal emergency affects work. HR can provide support and resources.

EAP offers confidential counseling. Emergency leave available.

We support employees during difficult times.

Travel Emergencies
Register international travel with security team. Emergency assistance available 24/7.

Travel insurance covers medical emergencies and evacuation. Keep emergency contact card with you.

Contact security team if emergency while traveling for business.

Reporting Non-Emergency Issues
Facilities issues: Submit ticket via facilities portal

IT issues: Submit ticket via IT helpdesk portal

HR questions: Email hr@company.com or call during business hours

Security concerns: Email security@company.com
""",

    "general/collaboration_tools_guide.txt": """Collaboration Tools Guide

Slack - Team Communication
Primary tool for daily communication. Channels for teams, projects, and topics.

Direct messages for private conversations. Use threads to organize discussions.

Integrate with other tools (Google Calendar, Jira, GitHub). Mobile app for on-the-go access.

Google Workspace - Documents and Email
Gmail for email. Google Drive for file storage and sharing.

Google Docs for documents. Google Sheets for spreadsheets. Google Slides for presentations.

Real-time collaboration on documents. Comment and suggest features for feedback.

Zoom - Video Conferencing
Video meetings and webinars. Screen sharing and recording capabilities.

Breakout rooms for small group discussions. Virtual backgrounds for privacy.

Calendar integration for easy scheduling. Mobile app for remote joining.

Jira - Project Management
Track projects, tasks, and bugs. Agile boards for sprint planning.

Custom workflows for different teams. Reporting and dashboards for visibility.

Integration with development tools. Mobile app for updates on the go.

Confluence - Documentation
Team wiki and knowledge base. Document processes, decisions, and information.

Templates for common document types. Version history and page permissions.

Search functionality to find information. Integration with Jira for project documentation.

GitHub - Code Collaboration
Version control for code. Pull requests for code review.

Issues for bug tracking and feature requests. Actions for CI/CD automation.

Project boards for development planning. Security scanning and dependency management.

Figma - Design Collaboration
UI/UX design and prototyping. Real-time collaboration on designs.

Component libraries for consistency. Developer handoff with specs and assets.

Version history and branching. Comments for feedback and discussion.

Miro - Visual Collaboration
Virtual whiteboard for brainstorming. Templates for workshops and planning.

Real-time collaboration with remote teams. Sticky notes, diagrams, and drawings.

Integration with other tools. Export and share boards.

1Password - Password Management
Secure password storage and generation. Shared vaults for team passwords.

Browser extensions for auto-fill. Mobile apps for access anywhere.

Security audit and breach monitoring. Emergency access for account recovery.

Google Calendar - Scheduling
Schedule meetings and events. Share calendars with team.

Find meeting times with scheduling assistant. Set working hours and location.

Integrate with Zoom for video meetings. Mobile app for calendar on the go.

Tool Access and Setup
New employees receive access during onboarding. IT provisions accounts and licenses.

Training resources available in employee portal. Helpdesk support for tool issues.

Request additional tools through IT portal.

Best Practices
Use right tool for the task. Keep tools updated. Enable notifications appropriately.

Organize files and channels logically. Archive old projects and channels.

Integrate tools to reduce context switching. Provide feedback on tool effectiveness.

Mobile Access
Most tools have mobile apps. Install on company or personal device (with MDM).

Mobile access for flexibility and remote work. Secure mobile access with MFA.

Be mindful of data usage and security on mobile.

Tool Training
Self-paced training available for all tools. Live training sessions offered quarterly.

Tool champions in each team provide peer support. Documentation and tips in Confluence.

Request specific training through HR.

Security Considerations
Use strong passwords and MFA for all tools. Don't share credentials.

Follow data classification guidelines when sharing. Review and revoke unnecessary access.

Report security concerns to IT security team.
""",

    "general/brand_voice_guidelines.txt": """Brand Voice and Communication Guidelines

Brand Personality
Professional yet approachable. Confident but not arrogant. Innovative and forward-thinking.

Helpful and supportive. Clear and straightforward. Human and authentic.

Our Tone
Conversational: Write like you speak. Avoid corporate jargon and buzzwords.

Positive: Focus on solutions and possibilities. Encouraging and optimistic.

Respectful: Value diverse perspectives. Inclusive language. Professional without being stuffy.

Writing Style
Clear and concise: Get to the point. Use simple words. Short sentences and paragraphs.

Active voice: "We help you" not "You are helped by us."

Specific: Use concrete examples. Avoid vague statements. Back claims with evidence.

Voice Across Channels
Website: Professional, informative, persuasive. Focus on customer benefits.

Blog: Educational, thought leadership, conversational. Share insights and expertise.

Social Media: Engaging, timely, personality-driven. Join conversations authentically.

Email: Clear, actionable, respectful of recipient's time. Personalized when possible.

Support: Empathetic, patient, solution-focused. Acknowledge frustration and help resolve.

Grammar and Mechanics
Use proper grammar and spelling. Proofread before publishing.

Oxford comma for clarity. Contractions okay for conversational tone.

Numbers: Spell out one through nine, use numerals for 10+. Exceptions for dates, percentages, measurements.

Formatting
Headings: Clear and descriptive. Use hierarchy (H1, H2, H3).

Lists: Bullet points for unordered items. Numbered lists for steps or rankings.

Bold: Emphasize key points sparingly. Italics: For emphasis or titles.

Links: Descriptive link text, not "click here."

Inclusive Language
Gender-neutral: Use "they" as singular pronoun. "Salesperson" not "salesman."

Avoid assumptions about: Age, ability, race, religion, sexual orientation, family structure.

Person-first language: "Person with disability" not "disabled person."

Accessibility
Write for 8th-grade reading level for broad accessibility. Define technical terms.

Use alt text for images. Provide captions for videos. Ensure sufficient color contrast.

Structure content with headings for screen readers.

Brand Terminology
Product names: Capitalize and use consistently. Check brand guidelines for proper usage.

Company name: Full name on first mention, shortened form acceptable after.

Industry terms: Use standard terminology. Define acronyms on first use.

What to Avoid
Jargon and buzzwords: "Synergy," "leverage," "disrupt" (unless specific meaning).

Clichés: "Think outside the box," "game changer," "best of breed."

Hyperbole: "Revolutionary," "unprecedented," "world-class" (unless truly accurate).

Negative language: Focus on what we do, not what we don't.

Legal and Compliance
Claims must be accurate and substantiated. Avoid absolute statements ("always," "never").

Respect trademarks and copyrights. Include required disclosures and disclaimers.

Privacy policy and terms of service links where appropriate.

Review and Approval
Marketing reviews external communications. Legal reviews contracts and formal agreements.

Manager approval for significant communications. Peer review for important content.

Brand Guidelines
Full brand guidelines available in marketing portal. Includes: Logo usage, color palette, typography, imagery style.

Follow guidelines for consistency. Questions? Contact marketing team.

Continuous Improvement
Monitor audience response. Test different approaches. Learn from what works.

Stay current with communication trends. Evolve voice while maintaining core identity.

Provide feedback on brand voice effectiveness.
""",

    "general/meeting_etiquette.txt": """Meeting Etiquette and Best Practices

Before the Meeting
Send agenda at least 24 hours in advance. Include: Purpose, topics, time allocation, preparation needed.

Invite only necessary attendees. Specify required vs optional attendees.

Schedule during reasonable hours. Avoid back-to-back meetings when possible.

Book appropriate meeting room or video link. Test technology before important meetings.

Meeting Preparation
Review agenda and materials in advance. Prepare questions and contributions.

Complete any pre-work requested. Bring necessary materials and devices.

Arrive (or join) 2-3 minutes early. Test audio/video before video meetings.

Starting the Meeting
Start on time. Don't wait for latecomers beyond 2-3 minutes.

Review agenda and objectives. Confirm time allocation. Assign note-taker.

Set ground rules if needed (e.g., phones away, one person speaks at a time).

During the Meeting
Stay focused on agenda. One person speaks at a time. Listen actively.

Mute when not speaking (video meetings). Use video when possible for engagement.

Minimize distractions. Don't multitask. Put phones away.

Participate constructively. Ask questions. Share relevant insights.

Meeting Facilitation
Keep discussion on track. Manage time allocation. Ensure all voices heard.

Summarize key points and decisions. Capture action items with owners and deadlines.

Address conflicts constructively. Park off-topic items for later discussion.

Virtual Meeting Etiquette
Join with video on when possible. Professional background or virtual background.

Mute when not speaking. Use "raise hand" feature to speak.

Use chat for questions and links. Reactions for quick feedback.

Be present - don't multitask. Close unnecessary applications.

Meeting Participation
Contribute meaningfully. Don't dominate conversation. Encourage others to participate.

Build on others' ideas. Disagree respectfully. Focus on issues, not people.

Ask clarifying questions. Summarize to confirm understanding.

Ending the Meeting
Summarize decisions and action items. Confirm owners and deadlines.

Identify next steps and follow-up meetings. Thank participants.

End on time. If more time needed, check with attendees before extending.

After the Meeting
Send notes within 24 hours. Include: Decisions, action items, owners, deadlines.

Follow up on your action items. Update project management tools.

Provide feedback on meeting effectiveness.

Meeting Types
Stand-up: Brief (15 min), status updates, blockers. Stay standing to keep it short.

Brainstorming: Creative, open discussion, no bad ideas. Build on each other's thoughts.

Decision-making: Present options, discuss pros/cons, make decision. Document rationale.

Retrospective: Reflect on what worked and what didn't. Identify improvements.

One-on-one: Career development, feedback, personal check-in. Regular cadence.

Declining Meetings
Okay to decline if not necessary attendee. Explain why and suggest alternative.

Propose sending delegate if appropriate. Offer to review notes instead of attending.

Respect others' time by not requiring unnecessary attendance.

Meeting-Free Time
Some teams designate meeting-free times for focused work. Respect these blocks.

Consider meeting-free Fridays or afternoons. Batch meetings when possible.

Protect focus time on your calendar.

Effective Meetings
Clear purpose and agenda. Right people attending. Appropriate duration.

Active participation. Decisions made and documented. Action items assigned.

Follow-through on commitments. Continuous improvement of meeting practices.

When Not to Meet
Information can be shared via email or document. No discussion needed.

Decision already made - just communicate it. One-on-one conversation more appropriate.

Not enough preparation time. Key stakeholders unavailable.
""",

    "general/travel_faq.txt": """Business Travel Frequently Asked Questions

Travel Approval
Q: How far in advance should I request travel approval?
A: At least 2 weeks for domestic travel, 4 weeks for international. Earlier booking often means better rates.

Q: Who approves travel requests?
A: Manager approves domestic travel. International travel requires manager and finance approval.

Q: What if I need to travel on short notice?
A: Submit request ASAP with explanation. Emergency travel can be expedited.

Booking Travel
Q: How do I book flights and hotels?
A: Use company travel portal for corporate rates. IT will send login credentials during onboarding.

Q: Can I use my own travel rewards programs?
A: Yes, keep miles and points earned on business travel. Use for personal travel or upgrades.

Q: What class should I book?
A: Economy for domestic flights. Premium economy for international flights over 6 hours. Business class requires special approval.

Travel Expenses
Q: What expenses are reimbursable?
A: Flights, hotels, ground transportation, meals (with receipts), business-related expenses. See expense policy for details.

Q: Do I need receipts for everything?
A: Yes, for expenses over $25. Keep all receipts during travel.

Q: How do I get reimbursed?
A: Submit expense report within 1 week of return. Reimbursement processed within 10 business days.

International Travel
Q: Do I need a visa?
A: Depends on destination and your citizenship. Check requirements early - visa processing can take weeks.

Q: Will the company pay for my passport?
A: Yes, passport and visa costs for business travel are reimbursable.

Q: What about travel insurance?
A: Company provides travel insurance for international trips covering medical emergencies and evacuation.

Q: Should I notify anyone about international travel?
A: Yes, register travel with security team. Provide itinerary and emergency contacts.

Ground Transportation
Q: Can I rent a car?
A: Yes, if more economical than taxis/rideshare or if public transit inadequate. Book compact or mid-size.

Q: Are taxis and rideshares reimbursable?
A: Yes, with receipts. Use for airport transfers and business meetings.

Q: What about mileage if I drive my personal car?
A: Reimbursed at IRS standard rate. Submit mileage log with expense report.

Accommodations
Q: What's the hotel budget?
A: $200/night in major cities, $150/night elsewhere. Higher rates require justification and approval.

Q: Can I use Airbnb?
A: Yes, if comparable or lower cost than hotels and meets safety standards.

Q: What if I want to stay extra days for personal travel?
A: Okay at your expense. Book business portion separately or calculate business vs personal costs.

Meals and Entertainment
Q: What's the meal budget?
A: Reasonable expenses with receipts. Or use per diem ($75/day domestic, varies internationally).

Q: Can I expense client dinners?
A: Yes, with pre-approval and business justification. Include attendees and business purpose in expense report.

Q: Is alcohol reimbursable?
A: Only for client entertainment with approval. Not for personal meals.

Travel Safety
Q: What if there's an emergency while traveling?
A: Contact emergency hotline (888) 555-TRVL available 24/7. Also notify your manager.

Q: Should I register my travel?
A: Yes, especially international travel. Provides emergency assistance and tracking.

Q: What about travel to high-risk locations?
A: Requires special approval and additional security briefing. May require security escort.

Travel Changes
Q: What if I need to change my travel plans?
A: Contact travel portal support. Change fees reimbursable if business-related.

Q: What if my flight is cancelled?
A: Rebook through airline or travel portal. Additional expenses (hotel, meals) due to delays are reimbursable.

Q: Can I extend my trip for personal reasons?
A: Yes, at your expense. Ensure business portion is clearly separated in bookings and expenses.

Travel Advances
Q: Can I get money in advance for travel?
A: Yes, for international trips or extended domestic travel. Request through finance portal 1 week before travel.

Q: How do I reconcile a travel advance?
A: Submit expense report within 2 weeks of return. Repay unused advance or submit expenses to cover advance.

Other Questions
Q: What if I have dietary restrictions?
A: Inform travel coordinator for catered events. Choose appropriate restaurants for meals.

Q: Can I bring a family member?
A: At your expense. Company only covers business traveler's costs.

Q: What about travel vaccinations?
A: Required vaccinations for business travel are reimbursable. Consult travel clinic 6-8 weeks before travel.
""",

    "general/new_joiner_faq.txt": """New Employee Frequently Asked Questions

First Day
Q: What time should I arrive on my first day?
A: 10 AM unless told otherwise. You'll receive welcome email with details.

Q: What should I bring?
A: ID for paperwork, banking info for direct deposit. We'll provide everything else.

Q: What's the dress code?
A: Business casual. Jeans okay, just look professional. Dress up for client meetings.

Q: Will I get lunch?
A: Yes, we'll take you to lunch on your first day. Welcome to the team!

Onboarding
Q: How long is onboarding?
A: First week is orientation and setup. Full onboarding continues for 90 days with structured plan.

Q: What training will I receive?
A: Role-specific training from your team, company-wide training modules, and buddy support.

Q: Who is my onboarding buddy?
A: Assigned peer who helps you navigate the company. You'll meet them on day one.

Equipment and Access
Q: What equipment will I receive?
A: Laptop, monitor, keyboard, mouse, headset. Additional equipment based on role.

Q: When do I get system access?
A: Most access provisioned by day one. Additional access requested as needed through IT portal.

Q: Can I choose Mac or PC?
A: Yes, specify preference in pre-boarding survey. Most roles support either.

Benefits
Q: When do benefits start?
A: Health insurance starts day one. 401(k) after 3 months. Stock options vest over 4 years.

Q: How do I enroll in benefits?
A: Complete enrollment in HR portal during first week. HR will guide you through process.

Q: What if I miss the enrollment deadline?
A: You'll have to wait until next open enrollment unless you have qualifying life event.

Getting Started
Q: How do I learn what to do?
A: Your manager has 30-60-90 day plan. Start with onboarding tasks, then ramp up to real work.

Q: What if I have questions?
A: Ask your manager, buddy, or team members. No question is too small. We want you to succeed.

Q: How do I meet people?
A: Team introductions scheduled first week. Join social Slack channels. Attend company events.

Work Schedule
Q: What are my work hours?
A: Flexible schedule with core hours 10 AM - 4 PM. Discuss specific schedule with your manager.

Q: Can I work remotely?
A: Depends on role and manager preference. Many roles support remote or hybrid work.

Q: What about time off?
A: You start accruing PTO immediately. Can use after 90 days (or sooner with manager approval).

Communication
Q: What tools do we use?
A: Slack for chat, email for formal communication, Zoom for video, Google Workspace for documents.

Q: How do I know what meetings to attend?
A: Check your calendar. Your manager will add you to relevant recurring meetings.

Q: What if I'm confused about something?
A: Ask! Better to ask than guess wrong. Everyone was new once and remembers what it's like.

Performance
Q: When is my first performance review?
A: Informal check-ins at 30, 60, 90 days. First formal review at 6 months.

Q: How do I know if I'm doing well?
A: Regular feedback from manager. Ask for feedback proactively. No surprises at review time.

Q: What if I'm struggling?
A: Talk to your manager immediately. We provide support and resources. Early communication is key.

Career Development
Q: Are there growth opportunities?
A: Yes, we support career development through training, mentorship, and internal mobility.

Q: How do I learn about open positions?
A: Posted on internal job board. Current employees get first look before external posting.

Q: Can I change teams or roles?
A: Yes, after 12 months in current role. Discuss career interests with your manager.

Company Culture
Q: What's the culture like?
A: Collaborative, innovative, supportive. We value work-life balance and continuous learning.

Q: Are there social events?
A: Yes, team events, company events, interest-based groups. Participation optional but encouraged.

Q: How do I give feedback about the company?
A: Regular surveys, open door policy with management, suggestion box, or talk to HR.

Getting Help
Q: Who do I contact for IT issues?
A: IT helpdesk via portal, email, or phone. Available 24/7 for critical issues.

Q: Who handles HR questions?
A: Your HR business partner or hr@company.com.

Q: What if I have a problem?
A: Talk to your manager first. If not appropriate, contact HR or use ethics hotline.

Still Have Questions?
Check employee portal for policies and resources. Ask your buddy or manager. Contact HR anytime.

Welcome aboard! We're excited to have you on the team.
"""
}

def create_kb():
    """Create knowledge base directory structure and files"""
    base_dir = "knowledge_base"
    
    # Create base directory
    os.makedirs(base_dir, exist_ok=True)
    print(f"Created directory: {base_dir}/")
    
    # Create subdirectories
    subdirs = ["hr", "it", "finance", "security", "general"]
    for subdir in subdirs:
        path = os.path.join(base_dir, subdir)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}/")
    
    # Write all documents
    print("\nCreating documents...")
    for filepath, content in DOCUMENTS.items():
        full_path = os.path.join(base_dir, filepath)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"✓ Created: {filepath}")
    
    print(f"\n✅ Successfully created {len(DOCUMENTS)} documents in knowledge_base/")
    print("Knowledge base initialization complete!")

if __name__ == "__main__":
    create_kb()
