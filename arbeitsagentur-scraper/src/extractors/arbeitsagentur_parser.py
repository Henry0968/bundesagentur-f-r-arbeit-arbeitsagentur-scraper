thondef parse_job_listing(job):
return {
"employerName": job.get("employerName"),
"contractDuration": job.get("contractDuration"),
"jobType": job.get("jobType"),
"location": job.get("location"),
"salaryNote": job.get("salaryNote"),
"descriptionText": job.get("descriptionText"),
"title": job.get("title"),
"employerAddress": job.get("employerAddress"),
"externalURL": job.get("externalURL"),
}