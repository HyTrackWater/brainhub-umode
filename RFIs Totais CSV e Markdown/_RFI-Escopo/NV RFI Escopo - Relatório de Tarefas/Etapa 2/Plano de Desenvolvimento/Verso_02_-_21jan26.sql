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

  ju.name  AS created_by_name,
  ju.email AS created_by_email,

  ju2.name  AS completed_by_name,
  ju2.email AS completed_by_email,

  juopa.id          AS assignment_id,
  juopa.target_id   AS assignment_target_id,
  juopa.target_type AS assignment_target_type,
  juopa.record_id   AS assigned_record_id,
  juopa.record_type AS assigned_record_type,

  -- Assigned USER
  ju_assigned.name   AS assigned_user_name,
  ju_assigned.email  AS assigned_user_email,
  ju_assigned.status AS assigned_user_status,

  -- Assigned user's role/policy (now sourced from the valid-roles map)
  rv.policy_id   AS user_policy_assigned_id,
  pol_user.name  AS user_policy_assigned_name,

  -- Assigned POLICY (group/profile)
  pol.name AS assigned_policy_name,

  -- Task -> ProductDatasheet relationship
  jtr.id          AS task_relationship_id,
  jtr.record_type AS task_relationship_record_type,
  jtr.record_id   AS product_datasheet_id,

  -- Product (datasheet)
  p.collection_id AS collection_id,

  -- Collection + Brand
  c.name          AS collection_name,
  c.brand_id      AS brand_id,
  b.name          AS brand_name

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
 AND juopa.deleted_at IS NULL

LEFT JOIN umode_production.jumper_users ju_assigned
  ON juopa.record_type = 'J3::User'
 AND ju_assigned.id = juopa.record_id
 AND ju_assigned.deleted_at IS NULL

/* =========================================================
   VALID ROLES MAP (per user, entity 3357)
   - role status = 1 (active roles only)
   - policy_id NOT IN (935, 69)
   - pick one policy_id per user (MIN) to avoid row explosion
   ========================================================= */
LEFT JOIN (
  SELECT
    ur.user_id,
    MIN(ur.policy_id) AS policy_id
  FROM umode_production.user_roles ur
  WHERE ur.entity_id = 3357
    AND ur.status = 1
    AND ur.policy_id NOT IN (935, 69)
  GROUP BY ur.user_id
) rv
  ON juopa.record_type = 'J3::User'
 AND rv.user_id = juopa.record_id

LEFT JOIN umode_production.policies pol_user
  ON pol_user.id = rv.policy_id
 AND pol_user.entity_id = 3357
 AND pol_user.deleted_at IS NULL

LEFT JOIN umode_production.policies pol
  ON juopa.record_type = 'J3::Policy'
 AND pol.id = juopa.record_id
 AND pol.entity_id = 3357
 AND pol.deleted_at IS NULL

LEFT JOIN umode_production.jumper_task_relationships jtr
  ON jtr.task_id = jt.id
 AND jtr.record_type = 'ProductDatasheet'
 AND jtr.deleted_at IS NULL

LEFT JOIN umode_production.umode_products p
  ON p.id = jtr.record_id
 AND p.entity_id = 3357
 AND p.deleted_at IS NULL

LEFT JOIN umode_production.umode_collections c
  ON c.id = p.collection_id
 AND c.entity_id = 3357
 AND c.deleted_at IS NULL

LEFT JOIN umode_production.umode_brands b
  ON b.id = c.brand_id
 AND b.entity_id = 3357
 AND b.deleted_at IS NULL

WHERE jt.entity_id = 3357
  AND jt.deleted_at IS NULL

  -- Remove rows where the assigned user has an invalid email
  AND (
        juopa.record_type <> 'J3::User'
        OR (
             ju_assigned.email IS NOT NULL
             AND ju_assigned.email NOT LIKE '%inativo%'
             AND ju_assigned.email NOT LIKE '%@umode%'
           )
      )

  -- Remove rows where the assignment is a policy/group and the policy is excluded (935/69)
  AND (
        juopa.record_type <> 'J3::Policy'
        OR juopa.record_id NOT IN (935, 69)
      )

  -- Remove rows where the assignment is a user but the user has no valid active role
  AND (
        juopa.record_type <> 'J3::User'
        OR rv.user_id IS NOT NULL
      );