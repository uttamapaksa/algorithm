with frontends as (
    select sum(code) as code from skillcodes where category = 'Front End'
), pythons as (
    select code from skillcodes where name = 'Python'
), csharps as (
    select code from skillcodes where name = 'C#'
), grades as (
    select
    case
    when skill_code & (select code from frontends) and skill_code & (select code from pythons) then 'A'
    when skill_code & (select code from csharps) then 'B'
    when skill_code & (select code from frontends) then 'C'
    else 'F'
    end as grade,
    ID,
    email
    from DEVELOPERS
)

select *
from grades
where grade != 'F'
order by grade, id