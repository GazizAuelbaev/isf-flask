from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """

    <h2>Explain the three states of data: at rest, in transit, and in process. How does the protection of data differ in each state, and what
challenges arise in maintaining confidentiality, integrity, and availability?</h2>
Rest - data at rest stored on a physical or digital medium, such as hard drives, databases, or archives. You may face
unauthorized access, data recovery, key management.
Protection in rest: encryption, access controls, backups.
Transit - data in transit actively moving from one location to another, typically over a network, like when sending emails or
browsing websites, in some cases eavesdropping, data integrity, latency.
Protection in transit: Encryption (e.g., TLS/SSL), secure protocols, authentication.
Process - data in the process being actively used or manipulated by applications, services, or processes on a computer or
server.
Protection in process: access controls, encryption, error checking.
Chalenges in process: application vulnerabilities, data leakage, resource management.


    <h2>How does authorization control what a user can do on the network after successful authentication? b. Describe the attributes
used in the authorization process.</h2>
after successful authentication, authorization control dictates what actions or operations a user is allowed to perform within a
network or system. It ensures that users are granted appropriate permissions and access rights based on various attributes and
policies.
the attributes:
user id - its the unique code of any user that used by the sites etc
roles and groups - the user may have some role that was given by the companie
permission - the permission is when the user may do just some certain things
Access Control List - by ACL we may strick the rule of using some certain files, or access to some directories
Time based access - this access is the name said gives permission for some given time
Trust relationship - it when relationships between different systems or domains.


<h2>Provide examples and explanations of preventive, deterrent and detective access controls. How do compensative controls
support or substitute other controls in enforcing security policies?</h2>
Preventive Controls: Stop unauthorized access before it happens. Examples include authentication, access control lists, and
encryption.
Deterrent Controls: Discourage potential attackers through warning signs, security personnel, or access monitoring.
Detective Controls: Identify and respond to security incidents after they occur, like intrusion detection and log analysis.
Compensative Controls: Support or replace primary controls when they're ineffective. Examples include backups, training, and
redundancy.



<h2>Practical Task: Access Control List Implementation</h2>
Develop access control list by the following information:
create new directory dir
write the command, which will show you default ACL permissions for dir
create test.txt inside of the dir
owner of the test.txt Admin user
give full permission for new user maksat for /dir
<pre>mkdir newDir
getfacl newDir
cd newDir -> touch test.txt
chown Admin : Admin dir / test.txt
setfacl -m u:maksat:rwx dir
</pre>




    """

@app.route('/about')
def about():
    return 'About'
