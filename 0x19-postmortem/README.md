**Issue Summary:**

- **Duration:** 
  - Start Time: 12th November 2023, 10:00 AM (PST)
  - End Time: 12th November 2023, 1:30 PM (PST)
- **Impact:** 
  - The service experienced a complete outage, rendering the platform inaccessible for all users. Users attempting to access the platform encountered HTTP 503 errors. Approximately 100% of users were affected.
- **Root Cause:** 
  - An unexpected surge in database connections led to an overload, causing a cascading failure in the application servers.

**Timeline:**

- **Issue Detected:** 
  - 12th November 2023, 10:15 AM (PST)
- **Detection Method:** 
  - Monitoring alerts indicated a sudden spike in error rates and a significant increase in response times.
- **Actions Taken:** 
  - Investigation primarily focused on the application and database servers. Assumptions were made regarding potential DDoS attacks or database issues.
- **Misleading Paths:** 
  - Initially, the team assumed a DDoS attack due to the abrupt increase in traffic. Later, suspicions about database issues arose due to unusual query patterns.
- **Escalation:** 
  - The incident was escalated to the DevOps and Database Engineering teams for immediate intervention.
- **Resolution:** 
  - The root cause was identified as a misconfigured connection pool that exhausted available database connections. Temporary adjustments were made to the connection pool settings, and additional application server instances were provisioned to handle the load.

**Root Cause and Resolution:**

- **Cause:** 
  - A misconfigured connection pool led to an excessive number of open connections to the database server, surpassing its limits and causing a cascade failure in the application servers.
- **Resolution:** 
  - Immediate adjustments were made to the connection pool settings to restrict the number of concurrent connections. This helped stabilize the database and application servers. Additional servers were provisioned to distribute the load effectively.

**Corrective and Preventative Measures:**

- **Improvements:**
  - Implement enhanced monitoring for database connection usage and server performance metrics.
  - Conduct a thorough review and update of the database connection pooling configurations.
  - Develop and implement auto-scaling mechanisms for application servers to dynamically respond to increased loads.

- **Tasks to Address the Issue:**
  - Review and update database connection pool configurations to prevent future overload.
  - Implement automatic alerts and fail-safes in connection pooling settings to mitigate similar occurrences.
  - Perform a comprehensive stress test under various load conditions to ensure the system's ability to handle increased traffic without failure.

This incident highlighted the critical need for better monitoring and optimization of database connection pools. The implemented measures will prevent similar outages in the future and enhance the platform's reliability during unexpected spikes in user traffic.
