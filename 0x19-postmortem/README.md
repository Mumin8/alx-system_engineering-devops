On January 23, 2024, between 14:00 and 16:30 UTC, our system experienced a third-party service outage that affected the user authentication service. The impact resulted in service unavailability, rendering approximately 30% of users unable to log in.

Timeline:
Detection Time: January 23, 2024, 14:00 UTC
Detection Method: The issue was initially detected through monitoring alerts highlighting a spike in failed authentication attempts.
Actions Taken:
Our investigation focused on the user authentication service and its integration with the third-party provider.
Assumptions on the root cause included potential issues with API communication or a sudden change in third-party service endpoints.
Misleading Paths:
Initial investigations led us to explore potential database connection issues.
These paths were deemed irrelevant because subsequent analysis confirmed a functional database but highlighted issues with third-party API responses.
Escalation:
The incident was escalated to the DevOps and Integration Teams for further analysis and resolution.
Resolution:
The issue was resolved by updating our system's integration to accommodate recent changes in the third-party service API.
Root Cause and Resolution:

Root Cause:
The root cause of the third-party service outage was identified as a change in the authentication API structure of the third-party service, leading to failed authentication requests from our system.
Resolution:
To resolve the issue, we implemented an emergency update to our system's integration layer, ensuring compatibility with the modified API endpoints.
Corrective and Preventative Measures:

Improvements/Fixes:
Broadly speaking, improvements can be made in enhancing our monitoring systems to provide more granular insights into third-party service dependencies.
Tasks to Address the Issue:
Implement better monitoring for third-party service status, including proactive alerts for any changes in API structure.
Establish a backup mechanism for critical functionalities that can temporarily replace the third-party service during outages.
Develop a communication plan for users during third-party service outages, including real-time status updates on the login page.
