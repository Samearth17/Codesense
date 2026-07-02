# CodeSense Deployment Checklist

## Preflight

- [ ] `frontend/.env.local` contains the production `NEXT_PUBLIC_API_URL`.
- [ ] `backend/.env.local` has production-safe values.
- [ ] `backend/.env` and `frontend/.env` exist for Docker Compose if running containers locally.
- [ ] `ml/models/codesense_xgb.json` is present.
- [ ] `ml/models/model_meta.json` is present.

## Frontend: Vercel

- [ ] Project root is `frontend`.
- [ ] Build command is `npm run build`.
- [ ] Output directory is `.next`.
- [ ] `NEXT_PUBLIC_API_URL` points to the Render backend base URL.
- [ ] Production deployment opens `/scan` successfully.

## Backend: Render

- [ ] Service root is `backend`.
- [ ] Build command is `uv sync --frozen`.
- [ ] Start command is `uv run uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
- [ ] `APP_DEBUG=false`.
- [ ] `APP_ENV=production`.
- [ ] `BACKEND_CORS_ORIGINS` includes the exact Vercel frontend origin.
- [ ] `/health` returns `{"status":"ok","service":"codesense-backend"}`.

## Smoke Test

- [ ] Open the deployed frontend `/scan` page.
- [ ] Submit a valid Python function.
- [ ] Confirm a prediction card and feature breakdown render.
- [ ] Check Render logs for structured `http_request_completed` entries.
- [ ] Check browser console for no runtime errors.

## Rollback

- [ ] Keep the previous successful Vercel deployment available.
- [ ] Keep the previous successful Render deploy available.
- [ ] Revert environment variable changes before reverting code when diagnosing config-only failures.
