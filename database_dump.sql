--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';
SET default_table_access_method = heap;

--
-- Table: projects
--

CREATE TABLE public.projects (
    id integer NOT NULL,
    name character varying NOT NULL
);

CREATE SEQUENCE public.projects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;

ALTER TABLE ONLY public.projects
    ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);

CREATE INDEX ix_projects_id ON public.projects USING btree (id);

--
-- Table: users
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    email character varying NOT NULL,
    experience_level character varying NOT NULL,
    primary_stack character varying NOT NULL,
    preferred_duration character varying NOT NULL,
    skills character varying,
    availability_confirmed boolean NOT NULL
);

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;

ALTER TABLE ONLY public.users
    ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);

CREATE INDEX ix_users_id ON public.users USING btree (id);

--
-- Table: user_projects
--

CREATE TABLE public.user_projects (
    user_id integer NOT NULL,
    project_id integer NOT NULL
);

ALTER TABLE ONLY public.user_projects
    ADD CONSTRAINT user_projects_pkey PRIMARY KEY (user_id, project_id);

ALTER TABLE ONLY public.user_projects
    ADD CONSTRAINT user_projects_user_id_fkey
        FOREIGN KEY (user_id) REFERENCES public.users(id);

ALTER TABLE ONLY public.user_projects
    ADD CONSTRAINT user_projects_project_id_fkey
        FOREIGN KEY (project_id) REFERENCES public.projects(id);

--
-- Seed data: projects
--

COPY public.projects (id, name) FROM stdin;
1	Customer Portal Redesign
2	Data Pipeline Migration
3	Mobile App Enhancement
4	Internal Analytics Dashboard
5	API Gateway Implementation
6	Cloud Infrastructure Setup
7	E-commerce Platform Update
8	Reporting System Automation
9	Microservices Architecture Transition
10	Customer Data Platform Integration
\.

SELECT pg_catalog.setval('public.projects_id_seq', 10, true);
SELECT pg_catalog.setval('public.users_id_seq', 1, false);

--
-- PostgreSQL database dump complete
--