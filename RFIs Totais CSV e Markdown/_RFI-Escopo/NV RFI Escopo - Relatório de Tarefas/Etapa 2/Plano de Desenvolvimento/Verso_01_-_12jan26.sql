SELECT
  jt.entity_id AS entity_id,

  jt.id,
  jt.title,
  jt.description,
  jt.status,

  DATE_FORMAT(jt.deadline, '%d/%m/%Y')     AS deadline,
  DATE_FORMAT(jt.created_at, '%d/%m/%Y')   AS created_at,
  DATE_FORMAT(jt.updated_at, '%d/%m/%Y')   AS updated_at,
  DATE_FORMAT(jt.completed_at, '%d/%m/%Y') AS completed_at,

  jt.time,
  jt.created_by_id,
  jt.completed_by_id,

  jtt.name  AS task_type_name,
  jtt.color AS task_type_color,

  ju.name  AS created_by_name,
  ju.email AS created_by_email,

  ju2.name  AS completed_by_name,
  ju2.email AS completed_by_email,

  juopa.id        AS assignment_id,
  juopa.target_id AS assignment_task_id,
  juopa.record_id AS assigned_user_id,

  ju3.name  AS assigned_user_name,
  ju3.email AS assigned_user_email

FROM umode_production.jumper_tasks jt

JOIN umode_production.jumper_task_types jtt
  ON jtt.id = jt.task_type_id
 AND jtt.deleted_at IS NULL

JOIN umode_production.jumper_users ju
  ON ju.id = jt.created_by_id
 AND ju.deleted_at IS NULL

LEFT JOIN umode_production.jumper_users ju2
  ON ju2.id = jt.completed_by_id
 AND ju2.deleted_at IS NULL

LEFT JOIN umode_production.jumper_user_or_policy_accesses juopa
  ON juopa.target_type = 'J3::Task'
 AND juopa.target_id   = jt.id
 AND juopa.record_type = 'J3::User'
 AND juopa.deleted_at IS NULL

LEFT JOIN umode_production.jumper_users ju3
  ON ju3.id = juopa.record_id
 AND ju3.deleted_at IS NULL

WHERE jt.entity_id = 3357
  AND jt.deleted_at IS NULL;