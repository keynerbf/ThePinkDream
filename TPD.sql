--
-- PostgreSQL database dump
--

\restrict 6e66KyqWGa8Avotnq6gCo6DZDWMwENSE7mjFne3lw8skeWDpWaSJFbEijc29MtQ

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2025-10-08 13:08:51

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
-- TOC entry 217 (class 1259 OID 16575)
-- Name: detalle_pedidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detalle_pedidos (
    id integer NOT NULL,
    pedido_id integer,
    producto_id integer,
    cantidad integer NOT NULL,
    subtotal numeric(12,2) NOT NULL
);


ALTER TABLE public.detalle_pedidos OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16578)
-- Name: detalle_pedidos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detalle_pedidos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.detalle_pedidos_id_seq OWNER TO postgres;

--
-- TOC entry 4913 (class 0 OID 0)
-- Dependencies: 218
-- Name: detalle_pedidos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detalle_pedidos_id_seq OWNED BY public.detalle_pedidos.id;


--
-- TOC entry 219 (class 1259 OID 16579)
-- Name: pedidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedidos (
    id integer NOT NULL,
    usuario_id integer,
    direccion character varying(200) NOT NULL,
    metodo_pago character varying(50) NOT NULL,
    num_metodo_pago character varying(100) NOT NULL,
    productos character varying(1000) NOT NULL
);


ALTER TABLE public.pedidos OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16584)
-- Name: pagos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pagos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pagos_id_seq OWNER TO postgres;

--
-- TOC entry 4914 (class 0 OID 0)
-- Dependencies: 220
-- Name: pagos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pagos_id_seq OWNED BY public.pedidos.id;


--
-- TOC entry 221 (class 1259 OID 16585)
-- Name: productos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text,
    precio numeric(10,2) NOT NULL,
    imagen character varying(255)
);


ALTER TABLE public.productos OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16590)
-- Name: productos_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos_base (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text,
    precio numeric(10,2) NOT NULL,
    imagen character varying(255)
);


ALTER TABLE public.productos_base OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16595)
-- Name: productos_base_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos_base_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_base_id_seq OWNER TO postgres;

--
-- TOC entry 4915 (class 0 OID 0)
-- Dependencies: 223
-- Name: productos_base_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos_base_id_seq OWNED BY public.productos_base.id;


--
-- TOC entry 224 (class 1259 OID 16596)
-- Name: productos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_id_seq OWNER TO postgres;

--
-- TOC entry 4916 (class 0 OID 0)
-- Dependencies: 224
-- Name: productos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;


--
-- TOC entry 225 (class 1259 OID 16597)
-- Name: productos_nuevos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos_nuevos (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text,
    precio numeric(10,2) NOT NULL,
    imagen character varying(255)
);


ALTER TABLE public.productos_nuevos OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16602)
-- Name: productos_nuevos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos_nuevos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_nuevos_id_seq OWNER TO postgres;

--
-- TOC entry 4917 (class 0 OID 0)
-- Dependencies: 226
-- Name: productos_nuevos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos_nuevos_id_seq OWNED BY public.productos_nuevos.id;


--
-- TOC entry 227 (class 1259 OID 16603)
-- Name: productos_ofertas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos_ofertas (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text,
    precio numeric(10,2) NOT NULL,
    imagen character varying(255),
    descuento numeric(5,2) DEFAULT 0
);


ALTER TABLE public.productos_ofertas OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16609)
-- Name: productos_ofertas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.productos_ofertas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_ofertas_id_seq OWNER TO postgres;

--
-- TOC entry 4918 (class 0 OID 0)
-- Dependencies: 228
-- Name: productos_ofertas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.productos_ofertas_id_seq OWNED BY public.productos_ofertas.id;


--
-- TOC entry 229 (class 1259 OID 16610)
-- Name: registro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.registro (
    id integer NOT NULL,
    nombre_completo character varying NOT NULL,
    email character varying NOT NULL,
    "contraseña" character varying NOT NULL,
    rol character varying(20) DEFAULT 'usuario'::character varying
);


ALTER TABLE public.registro OWNER TO postgres;

--
-- TOC entry 4725 (class 2604 OID 16616)
-- Name: detalle_pedidos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_pedidos ALTER COLUMN id SET DEFAULT nextval('public.detalle_pedidos_id_seq'::regclass);


--
-- TOC entry 4726 (class 2604 OID 16617)
-- Name: pedidos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos ALTER COLUMN id SET DEFAULT nextval('public.pagos_id_seq'::regclass);


--
-- TOC entry 4727 (class 2604 OID 16618)
-- Name: productos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);


--
-- TOC entry 4728 (class 2604 OID 16619)
-- Name: productos_base id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_base ALTER COLUMN id SET DEFAULT nextval('public.productos_base_id_seq'::regclass);


--
-- TOC entry 4729 (class 2604 OID 16620)
-- Name: productos_nuevos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_nuevos ALTER COLUMN id SET DEFAULT nextval('public.productos_nuevos_id_seq'::regclass);


--
-- TOC entry 4730 (class 2604 OID 16621)
-- Name: productos_ofertas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_ofertas ALTER COLUMN id SET DEFAULT nextval('public.productos_ofertas_id_seq'::regclass);


--
-- TOC entry 4895 (class 0 OID 16575)
-- Dependencies: 217
-- Data for Name: detalle_pedidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detalle_pedidos (id, pedido_id, producto_id, cantidad, subtotal) FROM stdin;
\.


--
-- TOC entry 4897 (class 0 OID 16579)
-- Dependencies: 219
-- Data for Name: pedidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedidos (id, usuario_id, direccion, metodo_pago, num_metodo_pago, productos) FROM stdin;
2	1194964016	carrera 9m 84b 171	nequi	3246136165	Ramo Mixto (Oferta), Ramo de Tulipanes
3	1194964016	Carrera 13 #84-14	DaviPlata	3246136165	Ramo de Girasoles
4	1194964016	Carrera 13 #84-14	Nequi	3246136165	Ramo de Girasoles
5	1194964016	carrera 9m 84b 171	Nequi	3246136165	Ramo de Girasoles
6	1194964016	carrera 9m 84b 171	Nequi	3246136165	Ramo de Rosas Blancas, Ramo de Lirios Elegantes
7	12345	calle 2 carrera 21	Nequi	3132123121	Ramo de Girasoles
8	12345	calle 2 carrera 21	Tarjeta de crédito	121314414	Ramo de Rosas (Oferta)
9	12345	casdashduafsd	Nequi	3246136165	Ramo de Rosas Rojas
10	9999	mi casa	Tarjeta débito	12312424124	Ramo ejemplo
11	12345	Carrera 13 #84-14	Tarjeta débito	12312311231231231	Ramo de Girasoles
\.


--
-- TOC entry 4899 (class 0 OID 16585)
-- Dependencies: 221
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos (id, nombre, descripcion, precio, imagen) FROM stdin;
\.


--
-- TOC entry 4900 (class 0 OID 16590)
-- Dependencies: 222
-- Data for Name: productos_base; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos_base (id, nombre, descripcion, precio, imagen) FROM stdin;
1	Ramo de Rosas Rojas	\N	40000.00	/static/rojo.jpg
2	Ramo Mixto Colorido	\N	35000.00	/static/color_mixto.jpg
3	Ramo de Margaritas Blancas	\N	20000.00	/static/blancas_margaritas.jpg
4	Ramo de Tulipanes	\N	30000.00	/static/tulipanes_2.jpg
5	Ramo de Lirios Elegantes	\N	50000.00	/static/lirios.jpg
6	Ramo de Girasoles	\N	25000.00	/static/girasoles_2.jpg
7	Ramo de Orquídeas Exóticas	\N	60000.00	/static/orquideas.jpg
8	Ramo de Rosas Blancas	\N	45000.00	/static/blancas.jpg
9	Ramo Elegante con Rosas	\N	50000.00	/static/rosas_1.jpg
10	Ramo Clásico de Margaritas	None	30000.00	/static/margaritas_1.jpg
\.


--
-- TOC entry 4903 (class 0 OID 16597)
-- Dependencies: 225
-- Data for Name: productos_nuevos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos_nuevos (id, nombre, descripcion, precio, imagen) FROM stdin;
11	Ramo de Girasoles	\N	25000.00	/static/girasoles_1.jpg
12	Ramo de Tulipanes	\N	35000.00	/static/tulipanes_1.jpg
\.


--
-- TOC entry 4905 (class 0 OID 16603)
-- Dependencies: 227
-- Data for Name: productos_ofertas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos_ofertas (id, nombre, descripcion, precio, imagen, descuento) FROM stdin;
14	Ramo de Rosas (Oferta)	\N	25000.00	/static/oferta_rosas.jpg	0.00
15	Ramo Pequeño (Oferta)	\N	10000.00	/static/ramo_2.webp	0.00
13	Ramo Mixto (Oferta)	None	200000.00	/static/mixto.jpg	0.00
\.


--
-- TOC entry 4907 (class 0 OID 16610)
-- Dependencies: 229
-- Data for Name: registro; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.registro (id, nombre_completo, email, "contraseña", rol) FROM stdin;
11111111	David Fontalvo	keynerbeltranf@gmail.com	12345	usuario
12345	Keyner Beltran	keynerbeltranf@gmail.com	12345	usuario
9999	Admin Principal	admin@admin.com	admin123	admin
1194964016	Keyner Beltran Fontalvo	keynerbeltranf@gmail.com	keyner12345	admin
\.


--
-- TOC entry 4919 (class 0 OID 0)
-- Dependencies: 218
-- Name: detalle_pedidos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detalle_pedidos_id_seq', 1, false);


--
-- TOC entry 4920 (class 0 OID 0)
-- Dependencies: 220
-- Name: pagos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pagos_id_seq', 11, true);


--
-- TOC entry 4921 (class 0 OID 0)
-- Dependencies: 223
-- Name: productos_base_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos_base_id_seq', 10, true);


--
-- TOC entry 4922 (class 0 OID 0)
-- Dependencies: 224
-- Name: productos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos_id_seq', 1, false);


--
-- TOC entry 4923 (class 0 OID 0)
-- Dependencies: 226
-- Name: productos_nuevos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos_nuevos_id_seq', 2, true);


--
-- TOC entry 4924 (class 0 OID 0)
-- Dependencies: 228
-- Name: productos_ofertas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.productos_ofertas_id_seq', 3, true);


--
-- TOC entry 4734 (class 2606 OID 16623)
-- Name: detalle_pedidos detalle_pedidos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_pedidos
    ADD CONSTRAINT detalle_pedidos_pkey PRIMARY KEY (id);


--
-- TOC entry 4736 (class 2606 OID 16625)
-- Name: pedidos pagos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pagos_pkey PRIMARY KEY (id);


--
-- TOC entry 4740 (class 2606 OID 16627)
-- Name: productos_base productos_base_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_base
    ADD CONSTRAINT productos_base_pkey PRIMARY KEY (id);


--
-- TOC entry 4742 (class 2606 OID 16629)
-- Name: productos_nuevos productos_nuevos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_nuevos
    ADD CONSTRAINT productos_nuevos_pkey PRIMARY KEY (id);


--
-- TOC entry 4744 (class 2606 OID 16631)
-- Name: productos_ofertas productos_ofertas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos_ofertas
    ADD CONSTRAINT productos_ofertas_pkey PRIMARY KEY (id);


--
-- TOC entry 4738 (class 2606 OID 16633)
-- Name: productos productos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);


--
-- TOC entry 4746 (class 2606 OID 16635)
-- Name: registro registro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registro
    ADD CONSTRAINT registro_pkey PRIMARY KEY (id);


--
-- TOC entry 4747 (class 2606 OID 16636)
-- Name: detalle_pedidos detalle_pedidos_pedido_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_pedidos
    ADD CONSTRAINT detalle_pedidos_pedido_id_fkey FOREIGN KEY (pedido_id) REFERENCES public.pedidos(id) ON DELETE CASCADE;


--
-- TOC entry 4748 (class 2606 OID 16641)
-- Name: detalle_pedidos detalle_pedidos_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_pedidos
    ADD CONSTRAINT detalle_pedidos_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES public.productos(id) ON DELETE SET NULL;


--
-- TOC entry 4749 (class 2606 OID 16646)
-- Name: pedidos pagos_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedidos
    ADD CONSTRAINT pagos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.registro(id) ON DELETE CASCADE;


-- Completed on 2025-10-08 13:08:51

--
-- PostgreSQL database dump complete
--

\unrestrict 6e66KyqWGa8Avotnq6gCo6DZDWMwENSE7mjFne3lw8skeWDpWaSJFbEijc29MtQ

